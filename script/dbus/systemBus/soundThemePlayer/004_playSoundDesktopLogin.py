# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_playSoundDesktopLogin
# @Test Description:      播放系统登录音效
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
        self.Step("预制条件1:")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:播放音效")
        soundThemePlayer.playSoundDesktopLogin()

        self.CheckPoint("检查点1：检查播放音效成功")

    def tearDown(self):
        self.Step("收尾:")
