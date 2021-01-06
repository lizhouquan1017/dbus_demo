# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_fixErrTypeDependenciesBroken
# @Test Description:      创建一个修复DependenciesBroken错误的任务,检查更新源
# @Test Condition:
# @Test Step:             1.创建一个修复DependenciesBroken错误的任务；
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
        self.errType2 = self.get_data('errType2')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建一个DependenciesBroken错误的任务并检查成功")
        lastoreManager.fixError(self.errType2)

    def tearDown(self):
        self.Step("收尾:无")
