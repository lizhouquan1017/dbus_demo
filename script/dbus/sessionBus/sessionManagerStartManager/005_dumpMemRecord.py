# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_dumpMemRecord
# @Test Description:      DumpMemRecord () -> (string value),获取记录的应用程序进程内存占用信息。
# @Test Condition:        1.无
# @Test Step:             1.调用 DumpMemRecord 方法获取记录的应用程序进程内存占用信息
# @Test Result:           1.返回应用程序进程内存占用信息
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
        self.Step("步骤1:调用 DumpMemRecord 方法获取记录的应用程序进程内存占用信息")
        sessionManagerStartManager.dumpMemRecord()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
