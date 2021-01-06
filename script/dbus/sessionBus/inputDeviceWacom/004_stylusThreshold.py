# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_stylusThreshold
# @Test Description:      uint32 StylusThreshold (readwrite)
#                         触笔阈值
# @Test Condition:        无
# @Test Step:             1.读取 StylusThreshold 属性值
# @Test Result:           1.返回 uint32 类型数据
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
        self.Step("步骤1:读取 StylusThreshold 属性值")
        assert inputDeviceWacom.stylusThreshold()

    def tearDown(self):
        pass
