# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          009_isMemSufficient
# @Test Description:      IsMemSufficient () -> (bool value),检查内存是否充足
# @Test Condition:        1.无
# @Test Step:             1.调用 IsMemSufficient 方法检查内存是否充足
# @Test Result:           1.返回 Boolean 类型数据
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
        self.Step("步骤1:调用 IsMemSufficient 方法检查内存是否充足")
        sessionManagerStartManager.isMemSufficient()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
