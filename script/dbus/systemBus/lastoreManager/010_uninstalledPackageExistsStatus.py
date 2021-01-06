# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_uninstalledPackageExistsStatus
# @Test Description:      查询软件是否安装
# @Test Condition:
# @Test Step:             1.软件未安装，如123；
# @Test Result:           1.检查软件状态是否是未安装;
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
        self.Step("步骤1:查询未安装软件状态并查询成功")
        lastoreManager.packageExists('uninstall', self.uninstallPkgId)

    def tearDown(self):
        self.Step("收尾:无")
