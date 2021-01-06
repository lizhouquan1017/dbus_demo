# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getPresetGroups
# @Test Description:      根据账户类型获取用户组的信息
# @Test Condition:
# @Test Step:             1.执行getPresetGroups接口；
#
# @Test Result:           1.获取用户组的信息;
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
        self.Step("步骤1:执行getGroups接口，检查输出为普通用户组的信息")
        accounts.getPresetGroups(0)

        self.Step("步骤2:执行getGroups接口，检查输出为管理员用户组的信息")
        accounts.getPresetGroups(1)

    def tearDown(self):
        self.Step("收尾:")
