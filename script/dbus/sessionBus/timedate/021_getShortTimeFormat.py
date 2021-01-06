# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          021_getShortTimeFormat
# @Test Description:      短时间格式
# @Test Condition:
# @Test Step:             1.获取短时间格式值；
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
        self.Step("步骤1:获取短时间格式值，并检查获取成功")
        timedate.getShortTimeFormat()

    def tearDown(self):
        pass

