# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_getScreenScaleFactors
# @Test Description:      用于获取屏幕缩放比例，并返回字典对象.
# @Test Condition:        无
# @Test Step:             1.调用GetScreenScaleFactors函数，获取窗口缩放比例；
# @Test Result:           1.返回字典对象，每个屏幕名称对应的缩放比例，如{‘HDMI-0’：1.0}；
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
        self.Step("步骤1：调用GetScreenScaleFactors函数，获取屏幕的缩放比例")
        appearance.getScreenScaleFactors()

    def tearDown(self):
        self.Step("收尾：无")
