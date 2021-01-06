# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_getEntryIDs
# @Test Description:      GetEntryIDs() -> (string[] list),获取当前停靠在dock栏上的所有的引用id列表
#                         list: 应用的id字符串数组，id如deepin-music, google-chrome等等
# @Test Condition:        1.无
# @Test Step:             1.调用 GetEntryIDs 函数,判获取当前停靠在dock栏上的所有的引用id列表
# @Test Result:           1.返回 string[] list 类型数据
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
        self.Step("步骤1:调用 GetEntryIDs 函数,判获取当前停靠在dock栏上的所有的引用id列表")
        dock.getEntryIDs()

    def tearDown(self):
        self.Step("收尾:无")        
    

