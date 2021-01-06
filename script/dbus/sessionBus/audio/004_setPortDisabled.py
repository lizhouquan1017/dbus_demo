# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_setPortDisabled
# @Test Description:      禁用音频端口
# @Test Condition:
# @Test Step:             1.禁用音频端口；
# @Test Result:           1.检查禁用成功;
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

        self.Step("预制条件2:启用音频接口")
        audio.setPortEnabled(self.cardId, self.portName, 'enable')

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:禁用音频端口")
        audio.setPortEnabled(self.cardId, self.portName, 'disable')

        self.CheckPoint("检查点1：检查禁用音频端口成功")
        audio.checkSetPortEnabledStatus(self.cardId, self.portName, 'disable')

    def tearDown(self):
        self.Step("收尾:启用音频接口")
        audio.setPortEnabled(self.cardId, self.portName, 'enable')
