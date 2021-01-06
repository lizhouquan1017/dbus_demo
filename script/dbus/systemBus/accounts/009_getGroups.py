# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_getGroups.py
# @Test Description:      获取用户组的所有信息
# @Test Condition:
# @Test Step:             1.执行getGroups接口；
#
# @Test Result:           1.获取用户组的所有信息;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:执行getGroups接，检查输出为用户组的信息")
        accounts.getGroups()

    def tearDown(self):
        self.Step("收尾:")
