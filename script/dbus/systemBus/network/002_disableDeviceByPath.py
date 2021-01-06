# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_disableDeviceByPath
# @Test Description:      断开一个网络连接
# @Test Condition:
# @Test Step:             1.断开一个网络连接；
# @Test Result:           1.检查断开一个网络连接成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import sNetwork
from aw.dbus.sessionBus import dNetwork


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.netPath = self.get_data('netPath')

        self.Step("预制条件2:打开网络连接")
        dNetwork.enableDevice(self.netPath, 'enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:断开一个网络连接")
        sNetwork.enableDeviceByPath(self.netPath, 'disable')

        self.CheckPoint("检查点1:检查断开一个网络连接成功")
        sNetwork.checkEnableDeviceStatusByPath(self.netPath, 'disable')

    def tearDown(self):
        self.Step("收尾:打开网络连接")
        dNetwork.enableDevice(self.netPath, 'enable')
