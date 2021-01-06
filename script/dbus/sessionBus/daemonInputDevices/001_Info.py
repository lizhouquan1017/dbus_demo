# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_Info
# @Test Description:      InfoStruct[] Infos (read)
#
#                         type InfoStruct struct {
#                           string InterfaceName,
#                           string DeviceType
#                         }
#                         全部输入设备的接口
#                         字段含义:
#                                 InterfaceName : 设备的DBus接口名
#                                 DeviceType : 设备的类型
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 Infos 属性值
# @Test Result:           1.返回 InfoStruct[] 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************
import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import daemonInputDevices


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用接口读取 Infos 属性值")
        daemonInputDevices.infos()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
