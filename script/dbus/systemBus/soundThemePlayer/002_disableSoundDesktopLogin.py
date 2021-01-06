# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_disableSoundDesktopLogin
# @Test Description:      设置当前用户，登录时不播放音效
# @Test Condition:
# @Test Step:             1.关闭开机音效开关；
# @Test Result:           1.检查音效开关关闭成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import soundThemePlayer


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:关闭音效开关")
        soundThemePlayer.enableSoundDesktopLogin('disable')

        self.CheckPoint("检查点1：检查音效开关关闭成功")
        soundThemePlayer.checkSoundDesktopLoginStatus('disable')

    def tearDown(self):
        self.Step("收尾:打开音效开关")
        soundThemePlayer.enableSoundDesktopLogin('enable')
