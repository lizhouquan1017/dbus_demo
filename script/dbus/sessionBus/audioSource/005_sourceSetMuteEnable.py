# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_sourceSetMuteEnable
# @Test Description:      设置静音
# @Test Condition:
# @Test Step:             1.设置静音；
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
        self.value = True

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置静音")
        audioSource.sourceSetMute(self.value)

        self.CheckPoint("检查点1：检查设置成功")
        audioSource.checkSetMute(self.value)

    def tearDown(self):
        self.Step("收尾:无")
