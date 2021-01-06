# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_getJob
# @Test Description:      GetJob(jobId int64) -> (string)
#                         根据 id 获取相应的 job。
#                         返回 job 的 json 字符串表示。
# @Test Condition:        存在一个用户创建的job并获得其id
# @Test Step:             1.调用 GetJob 函数,获取job信息
# @Test Result:           1.返回 JSON 格式数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import calendarScheduler


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:创建一个job并获得其id")
        self.job_id = calendarScheduler.create_job(title='GetJob')
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GetJob 函数,获取job信息")
        calendarScheduler.getJob(self.job_id)
        time.sleep(2)

    def tearDown(self):
        self.Step("收尾:删除创建的job")
        calendarScheduler.delete_job(self.job_id)
        time.sleep(2)
