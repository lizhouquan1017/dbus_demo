# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_minimizeWindow
# @Test Description:      MinimizeWindow(win uint32),最小化给定id的窗口实例
#                         win: 请参考ActivateWindow函数的win参数
# @Test Condition:        1.打开一个文件管理器窗口
#                         2.获取文件管理器的窗口id
# @Test Step:             1.调用 MinimizeWindow 函数,传入文件管理器的窗口id
# @Test Result:           1.程序无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import subprocess

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dock


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:打开一个文件管理器窗口")
        self.p = subprocess.Popen('dde-file-manager')
        time.sleep(5)
        self.win_id = dock.get_window_id_by_name()
        time.sleep(1)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 MinimizeWindow 函数,传入文件管理器的窗口id")
        dock.minimizeWindow(self.win_id)

    def tearDown(self):
        self.Step("收尾:关闭文件管理器子进程")
        self.p.kill()
        time.sleep(2)
