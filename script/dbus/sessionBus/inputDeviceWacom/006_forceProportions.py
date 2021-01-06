# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_forceProportions
# @Test Description:      bool ForceProportions (readwrite)
#                         是否强制粗细均匀
# @Test Condition:        无
# @Test Step:             1.读取 ForceProportions 属性值
# @Test Result:           1.返回 bool 类型数据
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
        self.Step("步骤1:读取 ForceProportions 属性值")
        assert inputDeviceWacom.forceProportions()

    def tearDown(self):
        pass
