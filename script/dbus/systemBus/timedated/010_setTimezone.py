# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_setTimezone
# @Test Description:      设置时间区域
# @Test Condition:
# @Test Step:             1.设置时间区域；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import timedated


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置时间区域，并检查设置成功")
        timedated.setTimezone(self.passwd, 'Asia/Shanghai', '')

    def tearDown(self):
        self.Step("收尾:无")
