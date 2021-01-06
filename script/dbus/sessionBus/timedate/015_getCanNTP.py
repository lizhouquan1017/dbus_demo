# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_getCanNTP
# @Test Description:      获取是否能使用NTP时间服务器值
# @Test Condition:
# @Test Step:             1.获取是否能使用NTP时间服务器值；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取是否能使用NTP时间服务器值，并检查获取成功")
        timedate.getCanNTP()

    def tearDown(self):
        pass

