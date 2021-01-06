# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_sourceSetFade
# @Test Description:      设置前后声道平衡值
# @Test Condition:
# @Test Step:             1.设置前后声道平衡值；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSource


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.value = 0.0

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置前后声道平衡值")
        audioSource.sourceSetFade(self.value)

        self.CheckPoint("检查点1：检查设置成功")
        audioSource.checkSetFade(self.value)

    def tearDown(self):
        self.Step("收尾:无")
