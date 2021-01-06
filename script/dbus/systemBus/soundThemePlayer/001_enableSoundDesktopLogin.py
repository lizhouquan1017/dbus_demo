# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_enableSoundDesktopLogin
# @Test Description:      设置当前用户，登录时播放音效
# @Test Condition:
# @Test Step:             1.打开开机音效开关；
# @Test Result:           1.检查开机音效开关打开成功;
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
        self.Step("步骤1:打开开机音效开关")
        soundThemePlayer.enableSoundDesktopLogin('enable')

        self.CheckPoint("检查点1：检查开机音效开关打开成功")
        soundThemePlayer.checkSoundDesktopLoginStatus('enable')

    def tearDown(self):
        self.Step("收尾:")
