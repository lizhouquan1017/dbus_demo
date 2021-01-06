# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_isX11SessionActive
# @Test Description:      X11 Session是否活跃.
# @Test Condition:        无
# @Test Step:             1.调用IsX11SessionActive函数，查看X11 Session是否活跃；
# @Test Result:           1.返回Boolean类型数据;
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
        self.Step("步骤1：调用IsX11SessionActive函数，查看X11 Session是否活跃")
        sessionWatcher.isX11SessionActive()

    def tearDown(self):
        self.Step("收尾:无")
