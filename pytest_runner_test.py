# -*- coding:utf-8 -*-
import os
import sys
import logging
import subprocess

import pytest

from frame import constant
from frame.constant import root_path
from frame.get_parameters import get_build_parameters
from frame.ulogger import UnionTestLogger
from result_send2pms import send_all_result2pms


def get_case():
    """
    获取用例
    :return:case_list
    """
    path_ = os.path.join(root_path, "excute.txt")
    with open(path_, 'r') as f:
        content_list = f.readlines()
        case_list = [os.path.join(root_path, line.strip()[1:]) for line in content_list if line.strip()]
        f.close()

    return case_list


def excute_cmd(cmd):
    """
    执行cmd命令,输出内容
    :param cmd:输入的命令
    :return:命令执行内容输出
    """
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, encoding='utf-8')
    out_msg = p.stdout.read()
    err_msg = p.stderr.read()
    if err_msg:
        return err_msg
    else:
        return out_msg


def get_ip():
    command = 'ifconfig'
    content_list = os.popen(command).readlines()
    for content in content_list:
        content = content.strip()
        if content.startswith('inet') and not content.startswith('inet6'):
            _ = content.split(' ')
            ip = _[1]
            if ip != '127.0.0.1':
                return ip
    else:
        return 'N/A'


def get_dde_environment():
    """
    获取dde environment参数
    :return: None
    """
    allure_results_path = os.path.join(root_path, "allure-results")
    environment_file = os.path.join(allure_results_path, "environment.properties")
    uos_version = '20 Professional'
    device_ip = get_ip()
    dde_daemon_version = excute_cmd("dpkg -l |grep dde-daemon| awk '{if(\"dde-daemon\"==$2)print $3}'")
    dde_api_version = excute_cmd("dpkg -l |grep dde-api | awk '{if(\"dde-api\"==$2)print $3}'")
    startdde_version = excute_cmd("dpkg -l |grep startdde | awk '{if(\"startdde\"==$2)print $3}'")
    lastore_daemon_version = excute_cmd("dpkg -l |grep lastore-daemon | awk '{if(\"lastore-daemon\"==$2)print $3}'")

    info_dict = {'UOS_VERSION': uos_version,
                 'DEVICE_IP': device_ip,
                 'DDE_DAEMON_VERSION': dde_daemon_version,
                 'DDE_API_VERSION': dde_api_version,
                 'START_DDE_VERSION': startdde_version,
                 'LASTORE_DAEMON': lastore_daemon_version
                 }
    logging.info(info_dict)

    with open(environment_file, "w") as f:
        for key in info_dict:
            logging.info(f'{key}: {info_dict[key].strip()}')
            f.write(f'{key} = {info_dict[key].strip()}\n')

    categories_file = os.path.join(constant.resoure_path, 'categories.json')
    excute_cmd(f'cp {categories_file} {allure_results_path}')


def save_report_history():
    """
    处理history文件，allure生成趋势报告
    :return:None
    """
    allure_results_path = os.path.join(root_path, "allure-results")
    allure_report_path = os.path.join(root_path, 'allure-report')
    history_path = os.path.join(allure_report_path, 'history')

    if os.path.exists(allure_results_path):
        os.system(f'rm -r {allure_results_path}')
        os.makedirs(allure_results_path)

    if os.path.exists(history_path):
        excute_cmd(f'cp -r {history_path} {allure_results_path}')


if __name__ == '__main__':
    UnionTestLogger()
    get_build_parameters()
    marks = "-m public"
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            marks = f"{marks} or {item}"

    save_report_history()

    allure_results_path = 'allure-results'
    allure_report_path = 'allure-report'

    args = [marks, "-sq", "--alluredir", f"{allure_results_path}"]
    case_list = get_case()
    [args.append(item) for item in case_list]
    pytest.main(args)

    get_dde_environment()
    # os.system(f"allure generate --clean {allure_results_path} -o {allure_report_path}")
    send_all_result2pms()
