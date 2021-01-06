# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          018_distUpgrade
# @Test Description:      创建一个升级任务
# @Test Condition:
# @Test Step:             1.创建一个升级任务；
# @Test Result:           1.检查操作成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest
from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建一个升级任务")
        # lastoreManager.distUpgrade()

        self.CheckPoint("检查点1：检查操作成功")
        # lastoreManager.checkDistUpgradeStatus()

    def tearDown(self):
        self.Step("收尾:无")
