# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_getHasLidSwitch
# @Test Description:      判断是否有盒盖功能，有盒盖功能为true
# @Test Condition:
# @Test Step:             1.判断是否有盒盖功能，有盒盖功能为true
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import power


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:判断是否有盒盖功能检查读取成功")
        power.getHasLidSwitch()

    def tearDown(self):
        pass
