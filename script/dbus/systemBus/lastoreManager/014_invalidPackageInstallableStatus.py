# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          014_invalidPackageInstallableStatus
# @Test Description:      查询软件是否可以安装
# @Test Condition:
# @Test Step:             1.无效软件，如111；
# @Test Result:           1.检查软件是否可以安装;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.uninstallPkgId = self.get_data('uninstallPkgId')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:检查无效软件不可以安装")
        lastoreManager.packageInstallable('invalid', self.uninstallPkgId)

    def tearDown(self):
        self.Step("收尾:无")
