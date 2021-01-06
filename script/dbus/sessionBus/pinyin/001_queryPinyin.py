# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_queryPinyin
# @Test Description:      查询输入的汉字hans的拼音.
# @Test Condition:        无
# @Test Step:             1.调用Query函数，查询输入的汉字hans的拼音；
# @Test Result:           1.返回string[] list类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import pinyin
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.hans = "你好"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用Query函数，查询输入的汉字hans的拼音")
        pinyin.queryPinyin(self.hans)

    def tearDown(self):
        self.Step("收尾:无")
