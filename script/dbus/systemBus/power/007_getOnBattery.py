# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_getOnBattery
# @Test Description:      是否使用电池, 使用电池时为true
# @Test Condition:
# @Test Step:             1.是否使用电池, 使用电池时为true
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
        self.Step("步骤1:判断是否使用电池并检查读取成功")
        power.getOnBattery()

    def tearDown(self):
        pass
