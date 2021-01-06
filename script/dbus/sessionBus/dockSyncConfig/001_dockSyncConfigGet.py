# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_dockSyncConfigGet
# @Test Description:      获取配置信息.
# @Test Condition:        无
# @Test Step:             1.调用Get函数，获取配置信息；
# @Test Result:           1.cfgInfo:配置信息;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import dockSyncConfig
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用Get函数，获取配置信息")
        dockSyncConfig.dockSyncConfigGet()

    def tearDown(self):
        self.Step("收尾:无")
