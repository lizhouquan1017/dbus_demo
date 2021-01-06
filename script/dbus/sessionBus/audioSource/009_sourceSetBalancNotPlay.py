# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_sourceSetBalancNotPlay
# @Test Description:      设置左右声道平衡
# @Test Condition:
# @Test Step:             1.设置左右声道平衡，不播放声音反馈；
# # @Test Result:         1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSource


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.value = 0.2

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置左右声道平衡，不播放声音反馈")
        audioSource.sourceSetBalance(self.value, False)

        self.CheckPoint("检查点1：检查设置成功")
        audioSource.checkSetBalance(self.value)

    def tearDown(self):
        self.Step("收尾:无")
