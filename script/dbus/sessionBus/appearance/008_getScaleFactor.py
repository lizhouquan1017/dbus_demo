# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_getScaleFactor
# @Test Description:      用于获取窗口缩放比例，并返回设置的缩放比例（Double scale_factor）.
# @Test Condition:        无
# @Test Step:             1.调用GetScaleFactor函数，获取窗口缩放比例；
# @Test Result:           1.返回设置的缩放比例（Double scale_factor）；
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
        self.Step("步骤1：调用GetScaleFactor函数，获取设置的缩放比例")
        appearance.getScaleFactor()

    def tearDown(self):
        self.Step("收尾：无")
