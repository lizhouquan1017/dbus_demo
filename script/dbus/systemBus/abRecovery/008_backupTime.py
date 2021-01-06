# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          008_backupTime
# @Test Description:      int64 BackupTime
#                         备份时间 unix 时间戳
# @Test Condition:        1.完成备份一次
# @Test Step:             1.读取 BackupTime 属性值
# @Test Result:           1.返回 int64 类型数据
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
        self.Step("预制条件1:完成备份一次")
        abRecovery.start_backup()
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
        self.Step("步骤1:返回 int64 类型数据")
        abRecovery.backupTime()

    def tearDown(self):
        self.Step("收尾:无")
