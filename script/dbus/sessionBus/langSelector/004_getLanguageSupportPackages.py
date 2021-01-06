# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getLanguageSupportPackages
# @Test Description:      获取对应语言环境的语言支持包.
# @Test Condition:        无
# @Test Step:             1.调用GetLanguageSupportPackages函数，获取对应语言环境的语言支持包；
# @Test Result:           1.返回 []string 类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import langSelector
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.locale = langSelector.getLocale()

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用GetLanguageSupportPackages函数，获取对应语言环境的语言支持包")
        langSelector.getLanguageSupportPackages(self.locale)

    def tearDown(self):
        self.Step("收尾:无")
