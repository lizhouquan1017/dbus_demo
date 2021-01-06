# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_getJobs
# @Test Description:
#     """
#     GetJobs(startYear int32, startMonth int32, startDay int32,
#     endYear int32, endMonth int32, endDay int32) -> (string)
#     指定开始日期和结束日期。
#     返回 JSON 格式
#     [
#      {
#         "Date": "2019-01-01",
#         "Jobs": [ job1, job2, ... ],
#      }, ...
#     ]
#     @return:
#     """
# @Test Condition:       无
# @Test Step:            1.调用 GetJobs 函数,获取本年度所有的job
# @Test Result:          1.返回 JSON 格式数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import calendarScheduler


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GetJobs 函数,获取本年度所有的job")
        calendarScheduler.getJobs()

    def tearDown(self):
        self.Step("收尾:无")
