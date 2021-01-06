# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_noRestartPulseAudio
# @Test Description:      用于设置不自动重启 pulseaudio 服务
# @Test Condition:
# @Test Step:             1.用于设置不自动重启 pulseaudio 服务；
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
        self.Step("步骤1:用于设置不自动重启 pulseaudio 服务，并检查执行成功")
        audio.noRestartPulseAudio()

    def tearDown(self):
        self.Step("收尾:无")