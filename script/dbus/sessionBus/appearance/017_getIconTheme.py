# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          017_getIconTheme
# @Test Description:      用于获取当前用户设置的图标主题.
# @Test Condition:        无
# @Test Step:             1.获取当前用户设置的图标主题；
# @Test Result:           1.返回String类型数据；
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预置条件1：无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：获取当前用户设置的图标主题，返回String类型数据")
        appearance.getIconTheme()

    def tearDown(self):
        self.Step("收尾：无")
