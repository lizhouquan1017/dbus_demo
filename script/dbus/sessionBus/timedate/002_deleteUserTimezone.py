# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_deleteUserTimezone
# @Test Description:      从用户的时间区域列表中删除指定的时间区域
# @Test Condition:
# @Test Step:             1.从用户的时间区域列表中删除指定的时间区域；
# @Test Result:           1.检查删除成功;
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
        self.Step("步骤1:从用户的时间区域列表中删除指定的时间区域，并检查删除成功")
        timedate.deleteUserTimezone(self.zone)

    def tearDown(self):
        self.Step("收尾:添加时间区域到用户时间区域列表")
        timedate.addUserTimezone(self.zone)
