# -*- coding:utf-8 -*-

from frame import constant
from frame.base import OSBase
import os
import logging

base = OSBase()
run_loop = int(base.get_data("run_loop"))


def get_case():
    '''
    获取用例
    '''
    root_path = constant.root_path
    path_ = os.path.join(root_path, "excute.txt")
    with open(path_, 'r') as f:
        str_ = f.readlines()
        str_ = [x for x in str_ if x != '\n']
        f.close()
    list = []
    case_ = []
    for i in range(len(str_)):
        item1 = str_[i].split('/', 1)
        item2 = item1[1].split('.py')
        list_ = item2[0].replace('/', '.')
        i += 1
        list.append(list_)

    for item in range(len(list)):
        for loop in range(run_loop):
            case_.append(list[item])
            loop += 1
        item += 1
    return case_
