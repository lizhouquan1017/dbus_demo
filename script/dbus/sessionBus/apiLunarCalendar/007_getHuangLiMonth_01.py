# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_getHuangLiMonth_01
# @Test Description:      GetHuangLiMonth(int32 year, int32 month, bool fill) -> (string json),获取指定公历月的黄历信息
# @Test Condition:        1.无
# @Test Step:             1.调用 GetHuangLiMonth 函数,fill设置为false,获取指定公历月的黄历信息
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
        self.Step("步骤1:调用 GetHuangLiMonth 函数,fill设置为false,获取指定公历月的黄历信息")
        apiLunarCalendar.getHuangLiMonth(fill=False)

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
    

