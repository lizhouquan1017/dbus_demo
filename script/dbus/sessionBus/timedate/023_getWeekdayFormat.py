# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          023_getWeekdayFormat
# @Test Description:      星期格式
# @Test Condition:
# @Test Step:             1.获取星期格式值；
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
        self.Step("步骤1:获取星期格式值，并检查获取成功")
        timedate.getWeekdayFormat()

    def tearDown(self):
        pass

