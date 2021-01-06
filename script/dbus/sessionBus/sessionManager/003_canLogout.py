# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_canLogout
# @Test Description:      返回是否能注销，目前恒为true.
# @Test Condition:        无
# @Test Step:             1.调用CanLogout函数，返回是否能注销，目前恒为true；
# @Test Result:           1.value: 返回值恒为true;
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
        self.Step("步骤1：调用CanLogout函数，返回是否能注销，目前恒为true")
        sessionManager.canLogout()

    def tearDown(self):
        self.Step("收尾:无")
