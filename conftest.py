# -*- coding:utf-8 -*-
import sys
import copy

import pytest

from frame import constant
from result_send2pms import result_dict, info_dict_template

sys.path.append(constant.root_path)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    script_path = report.nodeid.split('::')[0]
    if script_path in result_dict:
        info_dict = result_dict[script_path]
    else:
        info_dict = copy.deepcopy(info_dict_template)
        result_dict[script_path] = info_dict

    # report相关信息参见 _pytest/reports.py::TestReport 源码
    info_dict['steps'][report.when]['result'] = report.outcome
    info_dict['steps'][report.when]['longrepr'] = str(report.longrepr)

    # call相关信息参见 _pytest/runner.py::CallInfo 源码
    # call.excinfo 为ExceptionInfo对象,相关信息参见 _pytest/_code/code.py::ExceptionInfo 源码
    # str(report.longrepr) 可以获取堆栈信息
    if call.excinfo:
        if AssertionError.__name__ == call.excinfo.typename:
            info_dict['result'] = 'fail'
            info_dict['longrepr'] = '测试不通过'
        else:
            info_dict['result'] = 'blocked'
            info_dict['longrepr'] = '测试发生错误'

    if report.when == 'teardown':
        if not info_dict['result']:
            info_dict['result'] = 'pass'
            info_dict['longrepr'] = '测试通过'
