# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_installedPackageExistsStatus
# @Test Description:      查询软件是否安装
# @Test Condition:
# @Test Step:             1.软件已安装，如deepin-music；
# @Test Result:           1.检查软件状态是否是已安装;
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
        self.Step("步骤1:查询已安装软件状态并查询成功")
        lastoreManager.packageExists('install', self.installPkgId)

    def tearDown(self):
        self.Step("收尾:无")
