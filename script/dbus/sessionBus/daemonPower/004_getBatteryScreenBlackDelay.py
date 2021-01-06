# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getBatteryScreenBlackDelay
# @Test Description:      Int32 read/write 使用电池时，不做任何操作，到关闭屏幕需要的时间 单位：秒 值为 0 时表示从不
# @Test Condition:
# @Test Step:             1.读取BatteryScreenBlackDelay属性值；
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
        self.Step("步骤1:读取BatteryScreenBlackDelay属性值，检查读取成功")
        daemonPower.getBatteryScreenBlackDelay()

    def tearDown(self):
        self.Step("收尾:无")
