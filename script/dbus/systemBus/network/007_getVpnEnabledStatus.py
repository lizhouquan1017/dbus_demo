# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_getVpnEnabledStatus
# @Test Description:      获取vpn功能是否启用
# @Test Condition:
# @Test Step:             1.获取vpn功能是否启用；
# @Test Result:           1.获取vpn功能状态成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import sNetwork


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取vpn功能是否启用状态并检查成功")
        sNetwork.getVpnEnableStatus()

    def tearDown(self):
        self.Step("收尾:无")
