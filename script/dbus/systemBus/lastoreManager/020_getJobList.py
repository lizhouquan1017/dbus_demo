# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          020_getJobList
# @Test Description:      获取任务列表
# @Test Condition:
# @Test Step:             1.获取任务列表；
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
        self.Step("步骤1:获取任务列表,并检查操作成功")
        lastoreManager.jobList()

    def tearDown(self):
        self.Step("收尾:无")
