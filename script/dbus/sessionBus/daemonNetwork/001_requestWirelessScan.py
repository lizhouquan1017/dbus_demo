# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_requestWirelessScan
# @Test Description:      函数体内增加被动刷新功能，每次被调用时，在触发扫描的同时，
#                         会收集并过滤wifi热点，并更新推送到前端，实现wifi列表被动1分钟刷新一次
# @Test Condition:
# @Test Step:             1.调用函数；
# @Test Result:           1.检查函数执行成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dNetwork


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用RequestWirelessScan函数")
        dNetwork.requestWirelessScan()

    def tearDown(self):
        self.Step("收尾:无")
