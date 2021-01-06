# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_setSoundTheme
# @Test Description:      设置声音主题
# @Test Condition:
# @Test Step:             1.进行声音主题设置；
# @Test Result:           1.检查声音主题设置成功;
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
        self.Step("步骤1:进行声音主题设置")
        soundThemePlayer.setSoundTheme('deepin')

        self.CheckPoint("检查点1：检查声音主题设置成功")
        soundThemePlayer.checksetSoundTheme('deepin')

    def tearDown(self):
        self.Step("收尾:")
