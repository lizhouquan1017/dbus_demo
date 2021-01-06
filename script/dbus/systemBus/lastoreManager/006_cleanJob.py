# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_cleanJob.py
# @Test Description:      清理一个任务，若任务正在运行，则暂停它
# @Test Condition:
# @Test Step:             1.清理一个任务，若任务正在运行，则暂停它；
# @Test Result:           1.检查清理成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.jobid = self.get_data('jobid')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建一个清理任务并检查成功")
        lastoreManager.cleanJob(self.jobid)

    def tearDown(self):
        self.Step("收尾:无")
