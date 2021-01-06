# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_getJobWithRule
# @Test Description:      GetJobsWithRule(int32 startYear, int32 startMonth, int32 startDay,
#                                         int32 endYear, int32 endMonth, int32 endDay , string rule) -> (string jobs)
#                          根据一个时间段的起始范围，以及日程的重复类型，返回需要的日程，返回的字符串为JSON格式字符串,
#                          目前共有五种重复类型：每日("FREQ=DAILY")，工作日("FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR"),
#                          每周("FREQ=WEEKLY")，每月("FREQ=MONTHLY")，每年("FREQ=YEARLY")
# @Test Condition:         无
# @Test Step:             1.调用 GetJobsWithRule 函数,获取全年日程中rule为YEARLY的日程
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
        self.Step("步骤1:调用 GetJobsWithRule 函数,获取全年日程中rule为YEARLY的日程")
        calendarScheduler.getJobWithRule('YEARLY')

    def tearDown(self):
        self.Step("收尾:无")
