# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_getUse24HourFormat
# @Test Description:      是否使用24小时时间制
# @Test Condition:
# @Test Step:             1.获取是否使用24小时时间制值；
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
        self.Step("步骤1:获取是否使用24小时时间制值，并检查获取成功")
        timedate.getUse24HourFormat()

    def tearDown(self):
        pass

