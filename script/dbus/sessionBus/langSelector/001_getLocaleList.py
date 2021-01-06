# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getLocaleList
# @Test Description:      获取系统支持的语言环境信息列表.
# @Test Condition:        无
# @Test Step:             1.调用GetLocaleList函数，获取系统支持的语言环境信息列表；
# @Test Result:           1.返回string[] list类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import langSelector
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用GetLocaleList函数，获取系统支持的语言环境信息列表")
        langSelector.getLocaleList()

    def tearDown(self):
        self.Step("收尾:无")
