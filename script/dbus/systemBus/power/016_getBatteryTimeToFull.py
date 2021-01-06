# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_getBatteryTimeToFull
# @Test Description:      电池充满时间，单位为秒
# @Test Condition:
# @Test Step:             1.读取电池充满时间值
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import power


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取电池充满时间值并检查读取成功")
        power.getBatteryTimeToFull()

    def tearDown(self):
        self.Step("收尾:无")
