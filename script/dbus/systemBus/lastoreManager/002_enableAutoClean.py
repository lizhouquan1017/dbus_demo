# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_enableAutoClean
# @Test Description:      自动清理
# @Test Condition:
# @Test Step:             1.自动清理；
# @Test Result:           1.检查打开成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:关闭自动清理")
        lastoreManager.setAutoClean('disable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:打开自动清理")
        lastoreManager.setAutoClean('enable')

        self.CheckPoint("检查点1：检查打开成功")
        lastoreManager.checkAutoCleanStatus('enable')

    def tearDown(self):
        self.Step("收尾:无")
