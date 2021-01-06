# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_getSinkVolume
# @Test Description:      当前音量
# @Test Condition:
# @Test Step:             1.读取Volume属性值；
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSink


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取Volume属性值，检查读取成功")
        audioSink.getSinkVolume()

    def tearDown(self):
        self.Step("收尾:无")
