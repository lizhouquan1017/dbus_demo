# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_queryList
# @Test Description:      查询输入的汉字hans的拼音，支持查询多组汉字词.
# @Test Condition:        无
# @Test Step:             1.调用QueryList函数，查询输入的汉字hans的拼音，支持查询多组汉字词；
# @Test Result:           1.返回json格式类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import pinyin
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.hans_list = ["你好", "武汉"]

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用QueryList函数，查询输入的汉字hans的拼音，支持查询多组汉字词")
        pinyin.QueryList(self.hans_list)

    def tearDown(self):
        self.Step("收尾:无")
