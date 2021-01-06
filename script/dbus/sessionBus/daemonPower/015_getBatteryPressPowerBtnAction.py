# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_getBatteryPressPowerBtnAction
# @Test Description:      使用电池按下电源键的操作：0:关机（默认）、1:待机、2:休眠、3:关屏、4:显示sessionUI
# @Test Condition:
# @Test Step:             1.读取BatteryPressPowerBtnAction属性值；
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
        self.Step("步骤1:读取BatteryPressPowerBtnAction属性值，检查读取成功")
        daemonPower.getBatteryPressPowerBtnAction()

    def tearDown(self):
        self.Step("收尾:无")
