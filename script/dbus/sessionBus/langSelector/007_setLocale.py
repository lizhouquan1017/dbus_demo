# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_setLocale
# @Test Description:      设置当前用户的桌面语言环境.
# @Test Condition:        无
# @Test Step:             1.调用SetLocale函数，设置当前用户的桌面语言环境；
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
        self.Step("步骤1：调用SetLocale函数，设置当前用户的桌面语言环境")
        langSelector.setLocale(self.locale)

    def tearDown(self):
        self.Step("收尾:无")