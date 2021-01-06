# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_getInhibitors
# @Test Description:      遍历得到 Inhibitor 的路径列表，Inhibitor 是操作拦截器的意思，可以阻止一些由 flags 指定的操作.
# @Test Condition:        无
# @Test Step:             1.调用GetInhibitors函数，遍历得到 Inhibitor 的路径列表，Inhibitor 是操作拦截器的意思，可以阻止一些由 flags 指定的操作；
# @Test Result:           1.ArrayofObjectPath: 返回一个包含 Inhibitors 路径名的数组;
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
        self.Step("步骤1：调用GetInhibitors函数，遍历得到 Inhibitor 的路径列表，Inhibitor 是操作拦截器的意思，可以阻止一些由 flags 指定的操作")
        sessionManager.getInhibitors()

    def tearDown(self):
        self.Step("收尾:无")
