# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_vpnEnabled
# @Test Description:      Boolean VpnEnabled (read/write),指示VPN功能开关是否开启
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 VpnEnabled 属性值
# @Test Result:           1.返回 Boolean 数据类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dNetwork


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用接口读取 VpnEnabled 属性值")
        dNetwork.vpnEnabled()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(2)
