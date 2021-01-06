# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          020_getShortDateFormat
# @Test Description:      短日期格式
# @Test Condition:
# @Test Step:             1.获取短日期格式值；
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

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取短日期格式值，并检查获取成功")
        timedate.getShortDateFormat()

    def tearDown(self):
        pass

