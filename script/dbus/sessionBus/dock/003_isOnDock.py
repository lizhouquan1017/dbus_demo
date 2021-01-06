# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_isOnDock
# @Test Description:      IsOnDock(string desktopFile) -> (bool value),判断指定的应用是否固定在dock状态栏，或者是否正在运行并且在dock栏存在关联icon参数
#                         desktopFile: 应用的DesktopFile文件路径字符串
#                         value: true表示固定在dock状态栏，或者运行并在dock栏存在关联icon
# @Test Condition:        1.无
# @Test Step:             1.调用 IsDocked 函数,判断指定的应用是否固定在dock状态栏，或者是否正在运行并且在dock栏存在关联icon参数,
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
        self.Step("步骤1:调用 IsDocked 函数,判断指定的应用是否固定在dock状态栏，或者是否正在运行并且在dock栏存在关联icon参数,\
                   DesktopFile使用/usr/share/applications/dde-file-manager.desktop")
        dock.isOnDock()

    def tearDown(self):
        self.Step("收尾:无")
