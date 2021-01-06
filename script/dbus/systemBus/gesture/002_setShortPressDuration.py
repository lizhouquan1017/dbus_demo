# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_setShortPressDuration
# @Test Description:      设置触控屏短按超时时间
# @Test Condition:
# @Test Step:             1.设置触控屏短按超时时间；
# @Test Result:           1.程序运行正常;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import gesture


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.duration = 200

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:设置触控屏短按超时时间，程序运行正常")
        gesture.setShortPressDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")