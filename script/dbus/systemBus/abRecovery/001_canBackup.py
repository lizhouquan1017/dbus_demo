# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_canBackup
# @Test Description:      CanBackup() -> (bool can)
#                         能否备份
#                         参数
#                             无
#                         返回
#                             can:能否备份
# @Test Condition:        1.无
# @Test Step:             1.调用 CanBackup 函数
# @Test Result:           1.返回 bool 类型数据
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
        self.Step("步骤1:调用 CanBackup 函数")
        abRecovery.canBackup()

    def tearDown(self):
        self.Step("收尾:无")        
    

