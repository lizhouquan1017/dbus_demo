# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_getShortPressDurationvalue
# @Test Description:      获取触控屏短按超时时间值
# @Test Condition:
# @Test Step:             1.获取触控屏短按超时时间值；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import gesture


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取触控屏短按超时时间值，并检查获取成功")
        gesture.getShortPressDurationValue()

    def tearDown(self):
        self.Step("收尾:无")