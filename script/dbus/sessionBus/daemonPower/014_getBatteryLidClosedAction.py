# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          014_getBatteryLidClosedAction
# @Test Description:      使用电池合上盖子的操作：0:关机、1:待机（默认）、2:休眠、3:关屏、4:无操作
# @Test Condition:
# @Test Step:             1.读取BatteryLidClosedAction属性值；
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
        self.Step("步骤1:读取BatteryLidClosedAction属性值，检查读取成功")
        daemonPower.getBatteryLidClosedAction()

    def tearDown(self):
        self.Step("收尾:无")
