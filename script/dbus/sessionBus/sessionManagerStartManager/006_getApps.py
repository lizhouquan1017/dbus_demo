# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_getApps
# @Test Description:      GetApps () -> (map[uint32]string value),得到App的序列号描述表
# @Test Condition:        1.无
# @Test Step:             1.调用 GetApps 方法获取App的序列号描述表
# @Test Result:           1.返回App的序列号描述表
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
        self.Step("步骤1:调用 GetApps 方法获取App的序列号描述表")
        sessionManagerStartManager.getApps()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
