# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_isAutostart_01
# @Test Description:      IsAutostart (string filename) -> (bool value),判断文件是否已经加入自动启动中
# @Test Condition:        1.将待测试文件添加到自启动
# @Test Step:             1.调用 IsAutostart 方法判断文件是否已经加入自动启动中
# @Test Result:           1.结果返回True
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import sessionManagerStartManager


class TestCase(OSBase):
    def setUp(self):
        logging.info(f'script{__file__.split("script")[1]}')
        self.Step("预制条件1:将待测试文件添加到自启动")
        self.file = r'/usr/share/applications/dde-file-manager.desktop'
        logging.info(f'待添加的自启动项path：{self.file}')
        sessionManagerStartManager.add_autostart(self.file)
        time.sleep(1)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 IsAutostart 方法判断文件是否已经加入自动启动中")
        sessionManagerStartManager.isAutostart(self.file, target=True)

    def tearDown(self):
        time.sleep(1)
        self.Step("收尾:移除自启动项")
        sessionManagerStartManager.remove_autostart(self.file)
        time.sleep(1)
