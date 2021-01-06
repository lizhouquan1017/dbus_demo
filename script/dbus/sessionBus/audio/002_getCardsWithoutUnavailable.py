# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_getCardsWithoutUnavailable
# @Test Description:      获取可用音频设备端口信息
# @Test Condition:
# @Test Step:             1.获取可用音频设备端口信息；
# @Test Result:           1.检查输出值不为空,则表示获取信息成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest
from frame.base import OSBase
from aw.dbus.sessionBus import audio


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取可用音频设备端口信息，并检查获取成功")
        audio.getCardsWithoutUnavailable()

    def tearDown(self):
        self.Step("收尾:无")
