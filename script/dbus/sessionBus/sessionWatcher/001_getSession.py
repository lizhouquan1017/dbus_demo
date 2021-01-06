# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getSession
# @Test Description:      获取所有Sessions的对象路径.
# @Test Condition:        无
# @Test Step:             1.调用GetSession函数，获取所有Sessions的对象路径；
# @Test Result:           1.返回Array类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import sessionWatcher
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用GetSession函数，获取所有Sessions的对象路径")
        sessionWatcher.getSessions()

    def tearDown(self):
        self.Step("收尾:无")
