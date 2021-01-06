# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          009_eraserRawSample
# @Test Description:      uint32 EraserRawSample (readwrite)
#                         擦除模式滑动采样窗口
# @Test Condition:        无
# @Test Step:             1.读取 EraserRawSample 属性值
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
        self.Step("步骤1:读取 EraserRawSample 属性值")
        assert inputDeviceWacom.eraserRawSample()

    def tearDown(self):
        pass
