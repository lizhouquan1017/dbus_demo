# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_queryJobs
# @Test Description:
#     """
#     QueryJobs(params string) -> (string)
#     params 为 JSON 格式：
#     {
#       "Key": "关键字",
#       "Start": "2019-09-27T17:00:00+08:00",
#       "End": "2019-09-27T18:00:00+08:00"
#     }
#     params 各字段用途：
#     Key 是关键字，用于看 Job 的 Title 字段值中是否有此字符串，会忽略两头的空白，如果为空，表示不使用关键字过滤条件。
#     Start 是查询时间段的开始时间，格式为 RFC3339，比如"2006-01-02T15:04:05+07:00"。
#     End 是查询时间段的结束时间，格式为 RFC3339，比如"2006-01-02T15:04:05+07:00"。
#     返回数据格式同 GetJobs。
#     :return:
#     """
# @Test Condition:       无
# @Test Step:            1.调用 QueryJobs 函数,获取本年度 Title 中包含"国庆"的job
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
        self.Step("步骤1:调用 QueryJobs 函数,获取本年度 Title 中包含'国庆'的job")
        calendarScheduler.queryJobs()

    def tearDown(self):
        self.Step("收尾:无")
