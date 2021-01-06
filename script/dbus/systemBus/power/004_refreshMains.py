# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_refreshMains
# @Test Description:      刷新电源适配器的状态
# @Test Condition:
# @Test Step:             1.刷新电源适配器的状态
# @Test Result:           1.检查刷新成功;
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
        self.Step("步骤1:刷新电源适配器的状态并检查刷新成功")
        power.refreshMains()

    def tearDown(self):
        pass
