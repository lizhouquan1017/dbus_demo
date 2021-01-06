# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getPowerSavingModeEnabled
# @Test Description:      表示节能模式是否开启
# @Test Condition:
# @Test Step:             1.读取节能模式是否开启值
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
        self.Step("步骤1:读取节能模式是否开启值并检查读取成功")
        power.getPowerSavingModeEnabled()

    def tearDown(self):
        pass
