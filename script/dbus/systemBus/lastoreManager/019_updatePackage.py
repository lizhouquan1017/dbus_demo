# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          019_updatePackage
# @Test Description:      升级软件包
# @Test Condition:
# @Test Step:             1.升级软件包；
# @Test Result:           1.检查操作成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.jobName = self.get_data('jobName')
        self.pkg = self.get_data('pkg')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:升级软件包,并检查操作成功")
        lastoreManager.updatePackage(self.jobName, self.pkg)

    def tearDown(self):
        self.Step("收尾:无")
