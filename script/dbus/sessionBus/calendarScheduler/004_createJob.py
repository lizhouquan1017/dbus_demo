# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_createJob
# @Test Description:      CreateJob(jobInfo string) -> (id int64)
#                         jobInfo 为 job 的字符串表示。
#                         返回新 job 的 id
# @Test Condition:        无
# @Test Step:             1.调用 CreateJob 函数,创建一个当日的日程
# @Test Result:           1.返回一个int64数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import calendarScheduler


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 CreateJob 函数,创建一个当日的日程")
        calendarScheduler.createJob()
        time.sleep(5)

    def tearDown(self):
        self.Step("收尾:无")
        job_id_list = calendarScheduler.get_job_id()
        calendarScheduler.clear_all_job(job_id_list)
        time.sleep(5)
