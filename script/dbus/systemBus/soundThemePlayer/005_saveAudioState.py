# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_saveAudioState
# @Test Description:      设置音频状态参数，数据会写入到配置文件
# @Test Condition:
# @Test Step:             1.设置音频状态参数；
# @Test Result:           1.检查设置音频状态参数成功;
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
        self.Step("步骤1:设置音频状态参数,并检查参数设置成功")
        soundThemePlayer.saveAudioState()

    def tearDown(self):
        self.Step("收尾:")
