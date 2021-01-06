# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_activateWindow
# @Test Description:      ActivateWindow(uint32 win),激活给定窗口id的已经打开的窗口，通常会使该窗口成为焦点窗口
#                         win: 窗口id，如何获取请查看Entry对象的WindowInfos属性
# @Test Condition:        1.打开一个文件管理器窗口
#                         2.获取文件管理器的窗口id
# @Test Step:             1.调用 ActivateWindow 函数,传入文件管理器的窗口id
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
        for i in range(3):
            self.p = subprocess.Popen('dde-file-manager')
            time.sleep(5)
            if i != 2:
                self.p.kill()
                time.sleep(3)
        self.win_id = dock.get_window_id_by_name()
        time.sleep(1)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 ActivateWindow 函数,传入文件管理器的窗口id")
        dock.activateWindow(self.win_id)

    def tearDown(self):
        self.Step("收尾:关闭文件管理器子进程")
        self.p.kill()
        time.sleep(2)
