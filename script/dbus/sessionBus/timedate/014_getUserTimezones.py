# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          014_getUserTimezones
# @Test Description:      获取用户添加的时间区域列表
# @Test Condition:
# @Test Step:             1.获取用户添加的时间区域列表；
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
        self.Step("步骤1:获取用户添加的时间区域列表，并检查获取成功")
        timedate.getUserTimezones()

    def tearDown(self):
        pass

