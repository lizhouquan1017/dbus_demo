# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_setLongPressDuration
# @Test Description:      设置触控屏长按超时时间
# @Test Condition:
# @Test Step:             1.设置触控屏长按超时时间；
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
        self.duration = 1000

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置触控屏长按超时时间")
        gesture.setLongPressDuration(self.duration)

        self.CheckPoint("检查点1：检查设置成功")
        gesture.checkSetLongPressDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")