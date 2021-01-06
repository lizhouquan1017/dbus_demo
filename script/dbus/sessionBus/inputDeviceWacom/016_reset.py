# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          016_reset
# @Test Description:      Reset() -> ()
#                         重置
# @Test Condition:        无
# @Test Step:             1.调用 Reset 函数
# @Test Result:           1.执行无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceWacom


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 Reset 函数")
        inputDeviceWacom.reset()

    def tearDown(self):
        self.Step("收尾:无")
