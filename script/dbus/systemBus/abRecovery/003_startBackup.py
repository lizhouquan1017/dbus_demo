# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_startBackup
# @Test Description:      StartBackup()
#                         开始备份
#                         参数
#                             无
#                         返回
#                             无
# @Test Condition:        1.无
# @Test Step:             1.调用 StartBackup 函数
# @Test Result:           1.成功调用无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import abRecovery


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 StartBackup 函数")
        abRecovery.startBackup()

    def tearDown(self):
        self.Step("收尾:无")
