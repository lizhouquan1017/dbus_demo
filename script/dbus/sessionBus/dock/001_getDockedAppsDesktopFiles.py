# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_getDockedAppsDesktopFiles
# @Test Description:      GetDockedAppsDesktopFiles() -> ([]string desktopFiles),获取当前所有固定在dock状态栏的引用的desktopFile路径数组
#                         desktopFiles: DesktopFile文件路径字符串数组
# @Test Condition:        1.无
# @Test Step:             1.调用 GetDockedAppsDesktopFiles 函数,获取当前所有固定在dock状态栏的引用的desktopFile路径数组
# @Test Result:           1.返回 []string desktopFiles 类型数据
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
        self.Step("步骤1:调用 GetDockedAppsDesktopFiles 函数,获取当前所有固定在dock状态栏的引用的desktopFile路径数组")
        dock.getDockedAppsDesktopFiles()

    def tearDown(self):
        self.Step("收尾:无")
