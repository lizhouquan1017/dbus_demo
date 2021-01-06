# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          019_displayMode
# @Test Description:      int32 DisplayMode:当前dock栏显示模式，0表示时尚模式，1表示高效模式
# @Test Condition:        1.无
# @Test Step:             1.读取属性 DisplayMode
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
        self.Step("步骤1:读取属性 DisplayMode")
        dock.displayMode()

    def tearDown(self):
        self.Step("收尾:无")
