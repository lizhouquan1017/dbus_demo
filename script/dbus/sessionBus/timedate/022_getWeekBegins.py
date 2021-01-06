# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          022_getWeekBegins
# @Test Description:      星期开始时间
# @Test Condition:
# @Test Step:             1.获取星期开始时间值；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取星期开始时间值，并检查获取成功")
        timedate.getWeekBegins()

    def tearDown(self):
        pass

