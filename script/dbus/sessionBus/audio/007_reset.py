# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_reset
# @Test Description:      用于重置输入输出设备的音量以及sound-effect的开关.
# @Test Condition:
# @Test Step:             1.用于重置输入输出设备的音量以及sound-effect的开关；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audio


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于重置输入输出设备的音量以及sound-effect的开关.，并检查执行成功")
        audio.reset()

    def tearDown(self):
        self.Step("收尾:无")