# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          009_reset
# @Test Description:      Reset() -> (),重置
# @Test Condition:        1.无
# @Test Step:             1.调用 Reset 方法重置
# @Test Result:           1.正常调用无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 Reset 方法重置")
        inputDeviceKeyboard.reset()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(5)
