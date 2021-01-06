# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_addAutostart_02
# @Test Description:      AddAutostart (string filename) -> (bool value),设置文件自动启动
# @Test Condition:        1.无
# @Test Step:             1.调用 AddAutostart 方法添加一个合法但不存在的文件（/usr/share/applications
#                           或~/.local/share/applications 文件夹在的desktop文件）
# @Test Result:           1.添加成功
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
        self.Step("预制条件1:无")
        self.file = r'/usr/share/applications/dde-file-manager-test.desktop'
        logging.info(f'待添加的自启动项path：{self.file}')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 AddAutostart 方法添加一个合法但不存在的文件")
        sessionManagerStartManager.addAutostart(self.file, err=True, err_type=2)

    def tearDown(self):
        time.sleep(1)
        self.Step("收尾:移除自启动项")
        sessionManagerStartManager.remove_autostart(self.file)
        time.sleep(1)
