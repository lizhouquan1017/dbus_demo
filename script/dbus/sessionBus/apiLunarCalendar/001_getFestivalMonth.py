# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_getFestivalMonth
# @Test Description:      GetFestivalMonth (int32 year, int32 month) -> (String json),获取指定公历月的假日信息
# @Test Condition:        1.无
# @Test Step:             1.调用 GetFestivalMonth 函数,获取指定公历月的假日信息
# @Test Result:           1.返回 String json 类型数据 或 null
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
        self.Step("步骤1:调用 GetFestivalMonth 函数,获取指定公历月的假日信息")
        apiLunarCalendar.getFestivalMonth()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
    

