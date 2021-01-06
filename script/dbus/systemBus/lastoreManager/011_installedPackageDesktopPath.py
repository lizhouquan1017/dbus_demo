# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_installedPackageDesktopPath
# @Test Description:      获取软件的执行路径
# @Test Condition:
# @Test Step:             1.软件已安装，如deepin-music；
# @Test Result:           1.检查软件的执行路径;
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
        self.Step("步骤1:查询已安装软件的执行路径并查询成功")
        lastoreManager.packageDesktopPath('install', self.installPkgId)

    def tearDown(self):
        self.Step("收尾:无")
        pass
