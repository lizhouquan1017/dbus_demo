# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          012_uninstalledPackageDesktopPath
# @Test Description:      获取软件的执行路径
# @Test Condition:
# @Test Step:             1.软件未安装，如111；
# @Test Result:           1.检查未安装软件的执行路径是否为空;
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
        self.Step("步骤1:查询未安装软件的执行路径为空成功")
        lastoreManager.packageDesktopPath('uninstall', self.uninstallPkgId)

    def tearDown(self):
        self.Step("收尾:无")
