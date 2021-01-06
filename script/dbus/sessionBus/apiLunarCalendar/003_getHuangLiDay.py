# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_getHuangLiDay
# @Test Description:      GetHuangLiDay (int32 year, int32 month, int32 day) -> (string json),获取指定公历日的黄历信息
# @Test Condition:        1.无
# @Test Step:             1.调用 GetHuangLiDay 函数,获取指定公历日的黄历信息
# @Test Result:           1.返回 string json 类型数据
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
        self.Step("步骤1:调用 GetHuangLiDay 函数,获取指定公历日的黄历信息")
        apiLunarCalendar.getHuangLiDay()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
