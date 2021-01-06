# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_getLinePowerScreenBlackDelay
# @Test Description:      Int32 read/write 接通电源时，不做任何操作，到关闭屏幕需要的时间
# @Test Condition:
# @Test Step:             1.读取LinePowerScreenBlackDelay属性值；
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import daemonPower


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取LinePowerScreenBlackDelay属性值，检查读取成功")
        daemonPower.getLinePowerScreenBlackDelay()

    def tearDown(self):
        self.Step("收尾:无")
