# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_getFestivalsInRange
# @Test Description:      GetFestivalsInRange (string startDate, string endDate) -> ([]DayFestival result),获取一段时间内的节假日信息
# @Test Condition:        1.无
# @Test Step:             1.调用 GetFestivalsInRange 函数,获取一段时间内的节假日信息
# @Test Result:           1.返回 []DayFestival 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import apiLunarCalendar


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GetFestivalsInRange 函数,获取一段时间内的节假日信息")
        apiLunarCalendar.getFestivalsInRange()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
    

