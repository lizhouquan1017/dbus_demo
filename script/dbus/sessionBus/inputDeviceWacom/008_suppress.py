# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          008_suppress
# @Test Description:      uint32 Suppress (readwrite)
#                         变化量抑制等级，xy坐标变化大于这个值才有效，取值0～100
# @Test Condition:        无
# @Test Step:             1.读取 Suppress 属性值
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
        self.Step("步骤1:读取 KeyDownAction 属性值")
        assert inputDeviceWacom.suppress()

    def tearDown(self):
        pass
