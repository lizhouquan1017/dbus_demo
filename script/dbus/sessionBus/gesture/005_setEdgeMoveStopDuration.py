# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_setEdgeMoveStopDuration
# @Test Description:      设置出触控屏边缘划入后停留时间，默认值200ms
# @Test Condition:
# @Test Step:             1.设置出触控屏边缘划入后停留时间；
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
        self.duration = 500

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:设置出触控屏边缘划入后停留时间")
        gesture.setEdgeMoveStopDuration(self.duration)

        self.CheckPoint("检查点1：检查设置成功")
        gesture.checkSetEdgeMoveStopDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")