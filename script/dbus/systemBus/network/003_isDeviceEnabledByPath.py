# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_isDeviceEnabledByPath
# @Test Description:      判断一个网络设备是否启用(path)
# @Test Condition:
# @Test Step:             1.判断一个网络设备是否启用；
# @Test Result:           1.检查判断一个网络设备是否启用;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:打开一个网络连接")
        dNetwork.enableDevice(self.netPath, 'enable')

        self.Step("步骤2:判断打开一个网络连接")
        sNetwork.getIsDeviceEnabledByPath(self.netPath)

        self.Step("步骤3:断开一个网络连接")
        sNetwork.enableDeviceByPath(self.netPath, 'disable')

        self.Step("步骤4:判断断开一个网络连接")
        sNetwork.getIsDeviceEnabledByPath(self.netPath)

    def tearDown(self):
        self.Step("收尾:打开网络连接")
        dNetwork.enableDevice(self.netPath, 'enable')
