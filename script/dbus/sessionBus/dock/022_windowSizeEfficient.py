# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          022_windowSizeEfficient
# @Test Description:      uint32 WindowSizeEfficient:高效模式下dock栏高度，调节范围40～100
# @Test Condition:        1.无
# @Test Step:             1.读取属性 WindowSizeEfficient
# @Test Result:           1.返回一个 uint32 数据
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
        self.Step("步骤1:读取属性 WindowSizeEfficient")
        dock.windowSizeEfficient()

    def tearDown(self):
        self.Step("收尾:无")        
    

