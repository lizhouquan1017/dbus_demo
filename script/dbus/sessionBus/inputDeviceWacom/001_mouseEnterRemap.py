# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_mouseEnterRemap
# @Test Description:      bool MouseEnterRemap(readwrite)
#                         当属性为True时，开启鼠标自动映射，意味着，当鼠标移动到新屏幕的时候，当在新屏幕启用画笔时，此时实际操作的为当前控制板
#                         当属性为False时，关闭鼠标映射，当在扩展板操作时，鼠标自动映射到主显示屏的相应位置
# @Test Condition:        pass
# @Test Step:             1.读取 MouseEnterRemap 属性值
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

    @pytest.mark.sp2
    def test_step(self):
        self.Step("步骤1:读取MouseEnterRemap属性值")
        assert inputDeviceWacom.mouseEnterRemap()

    def tearDown(self):
        pass
