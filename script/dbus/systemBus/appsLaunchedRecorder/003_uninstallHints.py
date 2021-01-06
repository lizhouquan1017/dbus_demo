# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          uninstallHints
# @Test Description:      UninstallHints(string[] desktopFile)
#                         删除某个程序关联的一组desktopFile的记录应用是否启动过的状态信息
#                         参数
#                             desktopFile: 某个应用的所有desktopFile文件路径
#                         返回
#                             无
# @Test Condition:        1.无
# @Test Step:             1.调用 UninstallHints 函数,删除某个程序关联的一组desktopFile的记录应用是否启动过的状态信息
# @Test Result:           1.调用成功无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import appsLaunchedRecorder


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 UninstallHints 函数,删除某个程序关联的一组desktopFile的记录应用是否启动过的状态信息")
        appsLaunchedRecorder.uninstallHints('/usr/share/applications/dde-file-manager.desktop')

    def tearDown(self):
        self.Step("收尾:无")
