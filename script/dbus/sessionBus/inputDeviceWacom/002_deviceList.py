# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_deviceList
# @Test Description:      string DeviceList (read)
#                         设备列表
# @Test Condition:        无
# @Test Step:             1.读取 DeviceList 属性值
# @Test Result:           1.返回 string 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceWacom


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取DeviceList属性值")
        assert inputDeviceWacom.deviceList()

    def tearDown(self):
        pass
