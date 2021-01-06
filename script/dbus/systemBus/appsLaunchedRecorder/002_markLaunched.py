# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_markLaunched
# @Test Description:      MarkLaunched(string desktopFile)
#                         标记某个应用是否启动过
#                         参数
#                             desktopFile: 标记该应用启动过,标记以后该应用的id就不会出现在GetNew函数返回的结构中
#                         返回
#                             无
# @Test Condition:        1.无
# @Test Step:             1.调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表
#                         2.存在从未打开过应用,调用MarkLaunched标记第一个应用,不存在则标记任意一个已存在应用,如：dde-file-manager
# @Test Result:           2.调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表,被标记应用不在列表中或调用成功无报错
# @Test Remark:           只有通过launcher卸载的应用再次安装才会在从未打开使用过的应用列表中,暂无方案通过代码模拟这一过程,200901
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import appsLaunchedRecorder


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表")
        apps_list = appsLaunchedRecorder.get_all_new_apps()

        self.Step("步骤2:存在从未打开过应用,调用MarkLaunched标记第一个应用,不存在则标记任意一个已存在应用,如：dde-file-manager")
        if apps_list:
            appsLaunchedRecorder.markLaunched(apps_list[0])
            time.sleep(5)
            self.CheckPoint("调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表,被标记应用不在列表中")
            assert appsLaunchedRecorder.is_new_apps(apps_list[0], target=False)
        else:
            self.CheckPoint("调用成功无报错")
            appsLaunchedRecorder.markLaunched('/usr/share/applications/dde-file-manager.desktop')

    def tearDown(self):
        self.Step("收尾:无")
