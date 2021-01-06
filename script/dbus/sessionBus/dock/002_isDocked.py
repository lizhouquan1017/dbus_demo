# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_isDocked
# @Test Description:      IsDocked(string desktopFile) -> (bool value),判断指定的应用是否固定在dock状态栏
#                         desktopFile: 应用的DesktopFile文件路径字符串
#                         value: true表示指定的应用固定在dock状态栏，false表示没有固定
# @Test Condition:        1.无
# @Test Step:             1.调用 IsDocked 函数,判断指定的应用是否固定在dock状态栏,
#                           DesktopFile使用/usr/share/applications/dde-file-manager.desktop
# @Test Result:           1.返回 bool 类型数据
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
        self.Step("步骤1:调用 IsDocked 函数,判断指定的应用是否固定在dock状态栏,\
                   DesktopFile使用/usr/share/applications/dde-file-manager.desktop")
        dock.isDocked()

    def tearDown(self):
        self.Step("收尾:无")
