# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_restoring
# @Test Description:      bool Restoring
#                         是否正在恢复
# @Test Condition:        1.无
# @Test Step:             1.读取 Restoring 属性值
# @Test Result:           1.返回 False
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
        self.Step("步骤1:读取 Restoring 属性值")
        abRecovery.restoring(target=False)

    def tearDown(self):
        self.Step("收尾:无")        
    

