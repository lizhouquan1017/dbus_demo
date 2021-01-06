# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_setDisableNTP
# @Test Description:      设置系统时钟是否和网络时钟不同步
# @Test Condition:
# @Test Step:             1.设置系统时钟是否和网络时钟不同步；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import timedated


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置系统时钟是否和网络时钟不同步，并检查设置成功")
        timedated.setNTP(False, '')

    def tearDown(self):
        self.Step("收尾:无")
