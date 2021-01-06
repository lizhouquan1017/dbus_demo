# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_getMaxUIVolume
# @Test Description:      最大UI音量与 IncreaseVolume 有关.IncreaseVolume如果是true,最大音量为150%,IncreaseVolume如果是false,最大音量为100%
# @Test Condition:
# @Test Step:             1.读取MaxUIVolume属性值；
# @Test Result:           1.检查读取成功;
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
        self.Step("步骤1:读取MaxUIVolume属性值，检查读取成功")
        audio.getMaxUIVolume()

    def tearDown(self):
        self.Step("收尾:无")
