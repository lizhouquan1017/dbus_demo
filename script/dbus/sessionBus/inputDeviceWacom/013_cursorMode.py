# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          013_cursorMode
# @Test Description:      bool CursorMode (readwrite)
#                         光标模式，true相对模式(光标根据数位笔坐标变化量移动)，false绝对模式（光标跟随数位笔的绝对坐标）
# @Test Condition:        无
# @Test Step:             1.读取 CursorMode 属性值
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
        self.Step("步骤1:读取 CursorMode 属性值")
        assert inputDeviceWacom.cursorMode()

    def tearDown(self):
        self.Step("收尾:无")        
    

