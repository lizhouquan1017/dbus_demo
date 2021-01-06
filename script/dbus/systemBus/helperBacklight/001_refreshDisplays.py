# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_refreshDisplays
# @Test Description:      刷新显示设备列表
# @Test Condition:
# @Test Step:             1.刷新显示设备列表；
# @Test Result:           1.检查刷新成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import helperBacklight


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:刷新显示设备列表并检查成功")
        helperBacklight.refreshDisplays()

    def tearDown(self):
        self.Step("收尾:无")
