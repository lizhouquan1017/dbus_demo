# -*- coding: utf-8 -*-

#****************************************************
# @Test Case ID:          012_setTimeWithRelative
# @Test Description:      设置当前时间
# @Test Condition:
# @Test Step:             1.设置当前时间,将 usec 加到系统时间上；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
#*****************************************************

import pytest
from frame.base import OSBase
from aw.dbus.sessionBus import timedate

class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:关闭自动同步")
        timedate.setNTP(False)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置当前时间,将 usec 加到系统时间上，并检查设置成功")
        timedate.setTime(60000000, True)

    def tearDown(self):
        self.Step("收尾:开启自动同步")
        timedate.setNTP(True)
