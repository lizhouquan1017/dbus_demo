# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_getIsActive
# @Test Description:      检查是否存在着活跃Session.
# @Test Condition:        无
# @Test Step:             1.检查是否存在着活跃Session；
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
        self.Step("步骤1：检查是否存在着活跃Session，返回Boolean类型数据")
        sessionWatcher.getIsActive()

    def tearDown(self):
        self.Step("收尾:无")
