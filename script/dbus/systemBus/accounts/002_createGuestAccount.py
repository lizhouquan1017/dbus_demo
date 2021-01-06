# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_createGuestAccount
# @Test Description:      创建来宾账户
# @Test Condition:
# @Test Step:             1.创建来宾账户；
# @Test Result:           1.检查创建来宾账户成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.passwd = self.get_data('passwd')

        self.Step("预制条件1:删除所有已存在来宾账户")
        accounts.deleteAllGuestUser(self.passwd)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建来宾账户，并检查创建成功")
        accounts.createGuestAccount(self.passwd)

    def tearDown(self):
        self.Step("收尾:删除创建的来宾账户")
        accounts.deleteAllGuestUser(self.passwd)
