# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_toggleWirelessEnabled
# @Test Description:      切换无线网络状态
# @Test Condition:
# @Test Step:             1.切换无线网络状态；
# @Test Result:           1.检查切换成功;
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
        self.Step("步骤1:切换无线网络状态,并检查切换成功")
        sNetwork.toggleWirelessEnabled()

    def tearDown(self):
        self.Step("收尾:无")
