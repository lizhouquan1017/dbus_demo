# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          019_getLongTimeFormat
# @Test Description:      长时间格式
# @Test Condition:
# @Test Step:             1.获取长时间格式值；
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
        self.Step("步骤1:获取长时间格式值，并检查获取成功")
        timedate.getLongTimeFormat()

    def tearDown(self):
        pass

