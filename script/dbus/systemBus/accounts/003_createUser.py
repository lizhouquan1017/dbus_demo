# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_createUser
# @Test Description:      创建User账户
# @Test Condition:
# @Test Step:             1.创建User账户；
# @Test Result:           1.检查创建User账户成功;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建User账户")
        accounts.createUser(self.passwd, self.username)

        self.CheckPoint("检查点1：检查创建User账户成功")
        accounts.checkCreateUserStatus(self.username)

    def tearDown(self):
        self.Step("收尾:删除创建的User账户")
        accounts.deleteUser(self.passwd, self.username)
