# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getCurrentLocale
# @Test Description:      获取当前用户的桌面语言环境.
# @Test Condition:        无
# @Test Step:             1.获取当前用户的桌面语言环境；
# @Test Result:           1.返回 string 类型数据;
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
        self.Step("步骤1：获取当前用户的桌面语言环境")
        langSelector.getCurrentLocale()

    def tearDown(self):
        self.Step("收尾:将系统语言重置")
        langSelector.langSelectorReset()

