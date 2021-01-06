# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_addUserTimezone
# @Test Description:      添加指定的时间区域到用户的时间区域列表中
# @Test Condition:
# @Test Step:             1.添加指定的时间区域到用户的时间区域列表中；
# @Test Result:           1.检查添加成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.zone = 'Asia/Shanghai'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:添加指定的时间区域到用户的时间区域列表中，并检查添加成功")
        timedate.addUserTimezone(self.zone)

    def tearDown(self):
        self.Step("收尾:无")