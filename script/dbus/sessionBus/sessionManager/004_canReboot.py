# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_canReboot
# @Test Description:      通过调用Login1.Manager.CanReboot(0)测试是否能重启.
# @Test Condition:        无
# @Test Step:             1.调用CanReboot函数，通过调用Login1.Manager.CanReboot(0)测试是否能重启；
# @Test Result:           1.value: CanReboot(0) 返回 "yes" 即为true,有"na", "yes", "no", 和 "challenge" 4种返回值;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import sessionManager
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用CanReboot函数，通过调用Login1.Manager.CanReboot(0)测试是否能重启")
        sessionManager.canReboot()

    def tearDown(self):
        self.Step("收尾:无")
