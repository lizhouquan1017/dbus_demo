# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_play
# @Test Description:      播放指定主题、事件和设备的音效
# @Test Condition:
# @Test Step:             1.播放音效；
# @Test Result:           1.检查播放音效成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import soundThemePlayer


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.theme = 'deepin'
        self.device = "plughw:CARD=/var/lib/deepin-sound-player/config-*.json,DEV=/var/lib/deepin-sound-player/config-*.json"
        self.event = 'message'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:播放音效")
        soundThemePlayer.play(self.theme, self.device, self.event)

        self.CheckPoint("检查点1：检查播放音效成功")

    def tearDown(self):
        self.Step("收尾:")
