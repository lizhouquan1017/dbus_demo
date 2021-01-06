# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          016_hideState
# @Test Description:      int32 HideState (read)
#                         当前dock隐藏状态，0表示未知状态，1表示dock显示，2表示dock隐藏
#                         前端dde-dock监听该属性改变事件，根据监听到的值控制dock显示或者隐藏
# @Test Condition:        1.无
# @Test Step:             1.读取属性 HideState
# @Test Result:           1.返回一个int32数据,且数据是0, 1, 2中的一个
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
        self.Step("步骤1:读取属性 HideState")
        dock.hideState()

    def tearDown(self):
        self.Step("收尾:无")        
    

