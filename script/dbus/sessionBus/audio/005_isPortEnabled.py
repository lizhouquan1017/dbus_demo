# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_isPortEnabled
# @Test Description:      获取音频端口的启用/禁用状态
# @Test Condition:
# @Test Step:             1.获取音频端口的启用/禁用状态；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audio


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.cardId = 0
        self.portName = 'HDA NVidia'

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取音频端口的启用/禁用状态，并检查获取成功")
        audio.checkIsPortEnabled(self.cardId, self.portName)

    def tearDown(self):
        self.Step("收尾:无")