# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_sinkSetBalanceIsPlay
# @Test Description:      设置左右声道平衡
# @Test Condition:
# @Test Step:             1.设置左右声道平衡，播放声音反馈；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSink


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.value = 0.3

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置左右声道平衡，播放声音反馈")
        audioSink.sinkSetBalance(self.value, True)

        self.CheckPoint("检查点1：检查设置成功")
        audioSink.checkSetBalance(self.value)

    def tearDown(self):
        self.Step("收尾:无")
