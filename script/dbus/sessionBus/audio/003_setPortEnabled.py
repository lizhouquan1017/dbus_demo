# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_setPortEnabled
# @Test Description:      启用音频端口
# @Test Condition:
# @Test Step:             1.启用音频端口；
# @Test Result:           1.检查启用成功;
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

        self.Step("预制条件2:禁用音频接口")
        audio.setPortEnabled(self.cardId, self.portName, 'disable')

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:启用音频端口")
        audio.setPortEnabled(self.cardId, self.portName, 'enable')

        self.CheckPoint("检查点1：检查启用音频端口成功")
        audio.checkSetPortEnabledStatus(self.cardId, self.portName, 'enable')

    def tearDown(self):
        self.Step("收尾:无")