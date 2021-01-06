# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          017_prepareDistUpgrade
# @Test Description:      开启一个预更新的任务，并返回此任务的路径
# @Test Condition:
# @Test Step:             1.开启一个预更新的任务；
# @Test Result:           1.检查返回此任务的路径成功;
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
        self.Step("步骤1:创建一个更新源的任务")
        # lastoreManager.prepareDistUpgrade()

        self.CheckPoint("检查点1：检查操作成功")
        # lastoreManager.checkPrepareDistUpgradeStatus()

    def tearDown(self):
        self.Step("收尾:无")
        pass
