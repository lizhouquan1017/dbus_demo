# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_addLocale
# @Test Description:      增加系统语言环境选项.
# @Test Condition:        无
# @Test Step:             1.调用AddLocale函数，增加系统语言环境选项；
# @Test Result:           1.检查接口执行成功;
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
        self.Step("步骤1：调用AddLocale函数，增加系统语言环境选项")
        langSelector.addLocale(self.locale)

    def tearDown(self):
        self.Step("收尾:无")
