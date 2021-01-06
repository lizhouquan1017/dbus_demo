# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          025_getAccountType
# @Test Description:
# @Test Condition:
# @Test Step:             1.帐户类型 0普通用户  1系统用户；
# @Test Result:           1.检查用户为普通用户;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import user
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')
        self.username = self.get_data('username')

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:创建普通用户")
        accounts.createUser2(self.passwd, self.username, 0)

        self.CheckPoint("检查点1：检查用户类型为普通用户")
        user.accountType(self.passwd, self.username, 0)

        self.Step("步骤2:删除用户")
        accounts.deleteUser(self.passwd, self.username)

        self.Step("步骤3:创建系统用户")
        accounts.createUser2(self.passwd, self.username, 1)

        self.CheckPoint("检查点3：检查用户类型为系统用户")
        user.accountType(self.passwd, self.username, 1)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
