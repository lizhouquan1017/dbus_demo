# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_autostartList
# @Test Description:      AutostartList () -> ([]string value),获得自动启动的列表
# @Test Condition:        1.无
# @Test Step:             1.调用 AutostartList 方法获取自动启动列表
# @Test Result:           1.返回自启动列表
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 AutostartList 方法获取自动启动列表")
        sessionManagerStartManager.autostartList()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
