# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_canRestore
# @Test Description:      CanRestore() -> (bool can)
#                         能否恢复
#                         参数
#                             无
#                         返回
#                             can:能否恢复
# @Test Condition:        1.无
# @Test Step:             1.调用 CanRestore 函数
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
        self.Step("步骤1:调用 canRestore 函数")
        abRecovery.canRestore()

    def tearDown(self):
        self.Step("收尾:无")
