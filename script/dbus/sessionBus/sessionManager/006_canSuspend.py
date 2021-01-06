# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_canSuspend
# @Test Description:      根据是否有文件/sys/power/mem_sleep 判断是否能待机，如有根据Login1.Manager.CanSuspend 测试是否能待机.
# @Test Condition:        无
# @Test Step:             1.调用CanSuspend函数，根据是否有文件/sys/power/mem_sleep 判断是否能待机，如有根据Login1.Manager.CanSuspend 测试是否能待机；
# @Test Result:           1.value: /sys/power/mem_sleep存在且通过Login1.Manager.CanSuspend(0)的结果为"yes"返回true;
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
        self.Step("步骤1：调用CanSuspend函数，根据是否有文件/sys/power/mem_sleep 判断是否能待机，如有根据Login1.Manager.CanSuspend 测试是否能待机")
        sessionManager.canSuspend()

    def tearDown(self):
        self.Step("收尾:无")
