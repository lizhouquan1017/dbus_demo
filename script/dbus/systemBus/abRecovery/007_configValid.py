# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_configValid
# @Test Description:      bool ConfigValid
#                         是否配置文件正确无误
# @Test Condition:        1.无
# @Test Step:             1.读取 ConfigValid 属性值
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
        self.Step("步骤1:读取 ConfigValid 属性值")
        abRecovery.configValid()

    def tearDown(self):
        self.Step("收尾:无")
