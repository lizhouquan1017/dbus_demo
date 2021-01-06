# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          012_getGuestIcon
# @Test Description:      获取来宾用户的图标绝对路径
# @Test Condition:
# @Test Step:             1.执行属性-GuestIcon接口；
#
# @Test Result:           1.返回来宾用户的图标绝对路径;
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
        self.Step("步骤1:执行属性-GuestIcon接口，检查输出为来宾用户的图标绝对路径")
        accounts.getGuestIcon()

    def tearDown(self):
        self.Step("收尾:")
