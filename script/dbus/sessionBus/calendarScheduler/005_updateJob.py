# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_updateJob
# @Test Description:      UpdateJob(jobInfo string)
#                         jobInfo 为 job 的字符串表示
# @Test Condition:        已存在一个job,并获取其job信息
# @Test Step:             1.修改已存在job信息的title值
#                         2.调用 UpdateJob 函数,传入新的job信息
# @Test Result:           2.函数调用无异常,job title 变更为新值
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import calendarScheduler


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:创建一个job")
        self.job_id = calendarScheduler.create_job(title=f'UpdateJob{int(time.time())}')

        self.Step("预制条件2:获取其job信息")
        self.job_info = calendarScheduler.get_job_info_by_id(self.job_id)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:修改已存在job信息的title值")
        new_title = f'UpdateJob{int(time.time())}'

        self.Step("步骤2:调用 UpdateJob 函数,传入新的job信息")
        calendarScheduler.updateJob(self.job_info, key='Title', value=new_title)
        time.sleep(2)
        self.CheckPoint(2)
        assert calendarScheduler.get_job_title_by_id(self.job_id) == new_title
        time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
        job_id_list = calendarScheduler.get_job_id()
        calendarScheduler.clear_all_job(job_id_list)
        time.sleep(5)
