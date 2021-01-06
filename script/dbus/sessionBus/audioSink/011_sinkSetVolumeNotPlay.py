# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_sinkSetVolumeNotPlay
# @Test Description:      设置音量大小
# @Test Condition:
# @Test Step:             1.设置音量大小，不播放声音反馈；
# # @Test Result:         1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSink


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.value = 0.5

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置音量大小，不播放声音反馈")
        audioSink.sinkSetVolume(self.value, False)

        self.CheckPoint("检查点1：检查设置成功")
        audioSink.checkSetVolume(self.value)

    def tearDown(self):
        self.Step("收尾:无")
