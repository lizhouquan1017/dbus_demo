# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_getJobsWithLimit
# @Test Description:      GetJobsWithLimit(int32 startYear, int32 startMonth, int32 startDay,
#                         int32 endYear, int32 endMonth, int32 endDay , int32 maxNum) -> (string jobs)
#                         根据一个时间段的起始范围，以及需要的最大日程数量，返回需要的日程，返回的字符串为JSON格式字符串
# @Test Condition:        无
# @Test Step:             1.调用 GetJobsWithLimit 函数,获取全年日程
# @Test Result:           1.返回'null'或JSON格式字符串
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import calendarScheduler


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.sp2
    def test_step(self):
        self.Step("步骤1:调用 GetJobsWithLimit 函数,获取全年日程")
        calendarScheduler.getJobsWithLimit()

    def tearDown(self):
        self.Step("收尾:无")
