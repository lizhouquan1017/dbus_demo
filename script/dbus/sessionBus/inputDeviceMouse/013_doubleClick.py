# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          013_doubleClick
# @Test Description:      int32 DoubleClick (readwrite) 双击间隔
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 DoubleClick 属性值
# @Test Result:           1.返回 int32 数据类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceMouse


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用接口读取 DoubleClick 属性值")
        inputDeviceMouse.doubleClick()

    def tearDown(self):
        self.Step("收尾:无")        
    

