# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          021_frontendWindowRect
# @Test Description:      Rect FrontendWindowRect:当前dock栏形状大小
#                         Rect 的定义:
#                                 {
#                                     X, Y          int32
#                                     Width, Height uint32
#                                 }
#                         字段含义:
#                                 X, Y: 矩形X、Y坐标点
#                                Width, Height：矩形宽、高值
# @Test Condition:        1.无
# @Test Step:             1.读取属性 FrontendWindowRect
# @Test Result:           1.返回一个 dbus.Struct 数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dock


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:")
        dock.frontendWindowRect()

    def tearDown(self):
        self.Step("收尾:无")
