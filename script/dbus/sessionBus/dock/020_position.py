# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          020_position
# @Test Description:      int32 Position:当前屏幕dock栏所在位置，0表示屏幕上方，1表示屏幕右边，2表示屏幕下方，3表示屏幕左边
# @Test Condition:        1.无
# @Test Step:             1.读取属性 Position
# @Test Result:           1.返回一个 int32 数据
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
        self.Step("步骤1:读取属性 Position")
        dock.position()

    def tearDown(self):
        self.Step("收尾:无")
