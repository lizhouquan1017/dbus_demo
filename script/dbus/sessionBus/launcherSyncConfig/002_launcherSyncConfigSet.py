# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_launcherSyncConfigSet
# @Test Description:      设置配置信息.
# @Test Condition:        无
# @Test Step:             1.调用Set函数，设置配置信息；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import launcherSyncConfig
from aw.dbus.sessionBus.launcherSyncConfig import getSyncConfig
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.data = getSyncConfig()

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用Set函数，设置配置信息")
        launcherSyncConfig.launcherSyncConfigSet(self.data)

    def tearDown(self):
        self.Step("收尾:无")
