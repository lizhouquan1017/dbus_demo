# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_setDblclickDuration
# @Test Description:      设置双击超时时间
# @Test Condition:
# @Test Step:             1.设置双击超时时间；
# @Test Result:           1.检查接口运行正常;
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
        self.Step("步骤1:设置双击超时时间，检查接口运行正常")
        gesture.setDblclickDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")
