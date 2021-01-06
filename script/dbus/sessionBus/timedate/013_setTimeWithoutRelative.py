# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_setTimeWithoutRelative
# @Test Description:      设置当前时间
# @Test Condition:
# @Test Step:             1.设置当前时间,将 usec 设置为系统时间；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:关闭自动同步")
        timedate.setNTP(False)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置当前时间,将 usec 设置为系统时间，并检查设置成功")
        timedate.setTime(1595505311000000, False)

    def tearDown(self):
        self.Step("收尾:开启自动同步")
        timedate.setNTP(True)
