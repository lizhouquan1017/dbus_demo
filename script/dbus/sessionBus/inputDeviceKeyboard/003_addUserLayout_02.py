# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_addUserLayout_02
# @Test Description:      AddUserLayout(string layout) -> (),增加用户键盘布局
#                         参数 layout: 键盘布局
# @Test Condition:        1.清除所有layout
# @Test Step:             1.自定义一个布局名称，如：'ltest;'
#                         2.调用 AddUserLayout 方法，添加自定义layout，并检查是否引发‘invalid layout’错误
# @Test Result:           2.每一个布局都可添加成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:清除所有layout")
        inputDeviceKeyboard.clear_user_layouts()
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:自定义一个布局名称，如：'ltest;'")
        layout = 'ltest;'
        self.Step("步骤2:调用 AddUserLayout 方法，添加自定义layout，并检查是否引发‘invalid layout’错误")
        inputDeviceKeyboard.addUserLayout(layout, err=True)
        time.sleep(2)

    def tearDown(self):
        self.Step("收尾:添加cn;")
        inputDeviceKeyboard.addUserLayout('cn;')
        time.sleep(2)
