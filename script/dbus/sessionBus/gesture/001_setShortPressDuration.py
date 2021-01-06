# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_setShortPressDuration
# @Test Description:      设置触控屏短按超时时间
# @Test Condition:
# @Test Step:             1.设置触控屏短按超时时间；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import gesture


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.duration = 200

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:设置触控屏短按超时时间")
        gesture.setShortPressDuration(self.duration)

        self.CheckPoint("检查点1：检查设置成功")
        gesture.checkSetShortPressDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")