# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_allowSessionDaemonRun
# @Test Description:      相当于SessionManger的allowSessionDaemonRun字段的Get方法, 获得allowSessionDaemonRun的值.
# @Test Condition:        无
# @Test Step:             1.调用AllowSessionDaemonRun函数，获得allowSessionDaemonRun的值；
# @Test Result:           1.value: 返回SessionManger中字段allowSessionDaemonRun的值,true表示可以启动Session Daemon, false 表示不能启动;
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
        self.Step("步骤1：调用AllowSessionDaemonRun函数，获得allowSessionDaemonRun的值")
        sessionManager.allowSessionDaemonRun()

    def tearDown(self):
        self.Step("收尾:无")
