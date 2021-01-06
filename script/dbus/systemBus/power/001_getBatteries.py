# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getBatteries
# @Test Description:      获取所有的电池对象路径列表
# @Test Condition:
# @Test Step:             1.获取所有的电池对象路径列表；
# @Test Result:           1.检查获取成功;
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
        self.Step("步骤1:获取所有的电池对象路径列表并检查获取成功")
        power.getBatteries()

    def tearDown(self):
        pass
