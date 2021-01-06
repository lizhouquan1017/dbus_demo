# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          015_hideMode
# @Test Description:      int32 HideMode (read/write)
#                         隐藏模式，对应dock的三个状态值，0表示dock一直显示，1表示dock一直隐藏，3表示智能隐藏
#                         该属性由dde-dock前端程序通过dbus属性设置
# @Test Condition:        1.无
# @Test Step:             1.读取属性 HideMode
# @Test Result:           1.返回一个int32数据,且数据是0, 1, 3中的一个
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
        self.Step("步骤1:读取属性 HideMode")
        dock.hideMode()

    def tearDown(self):
        self.Step("收尾:无")        
    

