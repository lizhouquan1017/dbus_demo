# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_networkGetConnections
# @Test Description:      获取wifi连接配置信息
# @Test Condition:
# @Test Step:             1.执行NetworkGetConnections () ↦ (Array of [Byte] data)；
# @Test Result:           1.返回数据类型为dbus.Array;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import daemon


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:执行NetworkGetConnections ()，检查返回数据类型为dbus.Array正常")
        daemon.networkGetConnections()

    def tearDown(self):
        self.Step("收尾:无")
