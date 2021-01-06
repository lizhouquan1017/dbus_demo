# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_validPackageInstallableStatus
# @Test Description:      查询软件是否可以安装
# @Test Condition:
# @Test Step:             1.有效软件，如deepin-music；
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
        self.installPkgId = self.get_data('installPkgId')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:检查有效软件可以安装")
        lastoreManager.packageInstallable('valid', self.installPkgId)

    def tearDown(self):
        self.Step("收尾:无")
