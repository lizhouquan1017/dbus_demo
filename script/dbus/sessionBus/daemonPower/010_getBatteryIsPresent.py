# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getBatteryIsPresent
# @Test Description:      电池是否可用，返回 Dict of {String,Boolean}
#                         例如：{'BAT0':True}表示 BAT0 可用
# @Test Condition:
# @Test Step:             1.读取BatteryIsPresent属性值；
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
        self.Step("步骤1:读取BatteryIsPresent属性值，检查读取成功")
        daemonPower.getBatteryIsPresent()

    def tearDown(self):
        self.Step("收尾:无")
