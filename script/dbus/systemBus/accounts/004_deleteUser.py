# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_deleteUser
# @Test Description:      根据用户名删除用户账户
# @Test Condition:
# @Test Step:             1.删除账户；
# @Test Result:           1.检查删除账户成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')
        self.username = self.get_data('username')

        self.Step("预制条件2:创建账户")
        accounts.createUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:删除账户")
        accounts.deleteUser(self.passwd, self.username)

        self.CheckPoint("检查点1：检查删除账户成功")
        accounts.checkDeleteUserStatus(self.username)

    def tearDown(self):
        self.Step("收尾:")