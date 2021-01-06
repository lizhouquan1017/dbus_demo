# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_packagesDownloadSize
# @Test Description:      获取软件包的下载大小
# @Test Condition:
# @Test Step:             1.获取软件包的下载大小；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.pkgs = ['deepin-music']

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取软件包的下载大小")
        lastoreManager.packagesDownloadSize(self.pkgs)

    def tearDown(self):
        self.Step("收尾:无")
