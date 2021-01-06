# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_canHibernate
# @Test Description:      对Login1.Manager.CanHibernate进行封装, 测试系统是否支持休眠。.
# @Test Condition:        无
# @Test Step:             1.调用CanHibernate函数，对Login1.Manager.CanHibernate进行封装, 测试系统是否支持休眠。；
# @Test Result:           1.value: 对应Login1.Manager.CanHibernate(0)的返回值,"yes" 则返回为 True;
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
        self.Step("步骤1：调用CanHibernate函数，对Login1.Manager.CanHibernate进行封装, 测试系统是否支持休眠")
        sessionManager.canHibernate()

    def tearDown(self):
        self.Step("收尾:无")
