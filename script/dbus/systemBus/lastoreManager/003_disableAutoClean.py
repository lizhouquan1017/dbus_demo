# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_disableAutoClean
# @Test Description:      自动清理
# @Test Condition:
# @Test Step:             1.关闭自动清理；
# @Test Result:           1.检查关闭成功;
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
        self.Step("步骤1:关闭自动清理")
        lastoreManager.setAutoClean('disable')

        self.CheckPoint("检查点1：检查关闭成功")
        lastoreManager.checkAutoCleanStatus('disable')

    def tearDown(self):
        self.Step("收尾:打开自动清理")
        lastoreManager.setAutoClean('enable')
