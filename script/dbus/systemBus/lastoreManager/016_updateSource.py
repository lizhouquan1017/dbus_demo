# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_updateSource
# @Test Description:      创建一个更新源的任务，并返回任务的路径
# @Test Condition:
# @Test Step:             1.创建一个更新源的任务；
# @Test Result:           1.检查返回任务的路径成功;
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
        self.Step("步骤1:创建一个更新源的任务，并检查返回任务的路径成功")
        lastoreManager.updateSource()

    def tearDown(self):
        self.Step("收尾:无")
