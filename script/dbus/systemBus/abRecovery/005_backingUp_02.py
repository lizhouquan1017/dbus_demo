# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_backingUp_02
# @Test Description:      bool BackingUp
#                         是否正在备份
# @Test Condition:        1.不开启备份
# @Test Step:             1.读取 BackingUp 属性值
# @Test Result:           1.返回 False
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import abRecovery


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:不开启备份")
        time.sleep(2)
        for item in range(1, 200):
            if abRecovery.backing_up():
                time.sleep(5)
                logging.info(f'备份未结束,第{item}圈')
                continue
            else:
                logging.info('备份结束')
                break

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取BackingUp属性值")
        abRecovery.backingUp(target=False)

    def tearDown(self):
        self.Step("收尾:无")

