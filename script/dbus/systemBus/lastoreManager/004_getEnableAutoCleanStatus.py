# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getEnableAutoCleanStatus
# @Test Description:      获取自动清理状态
# @Test Condition:
# @Test Step:             1.打开自动清理；
# @Test Result:           1.检查获取自动清理状态成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:打开自动清理")
        lastoreManager.setAutoClean('enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:检查获取自动清理状态成功")
        lastoreManager.getAutoCleanStatus()

    def tearDown(self):
        self.Step("收尾:无")
