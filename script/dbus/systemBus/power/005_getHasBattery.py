# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_getHasBattery
# @Test Description:      判断是否有电池(台式机还是笔记本)
# @Test Condition:
# @Test Step:             1.判断是否有电池(台式机还是笔记本)
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
        self.Step("步骤1:判断是否有电池检查读取成功")
        power.getHasBattery()

    def tearDown(self):
        pass
