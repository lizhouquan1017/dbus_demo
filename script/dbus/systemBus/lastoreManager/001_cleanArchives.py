# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_cleanArchives
# @Test Description:      创建一个清理任务
# @Test Condition:
# @Test Step:             1.创建一个清理任务；
# @Test Result:           1.检查创建成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建一个清理任务并检查成功")
        lastoreManager.cleanArchives()

    def tearDown(self):
        self.Step("收尾:无")
