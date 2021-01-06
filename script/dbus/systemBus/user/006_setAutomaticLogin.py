# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_setAutomaticLogin
# @Test Description:
# @Test Condition:
# @Test Step:             1.设置用户自动登录；
# @Test Result:           1.检查设置用户自动登录;
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

        self.Step("预制条件3:设置账户密码")
        user.setPassword(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置自动登录")
        user.setAutomaticLogin(self.passwd, self.username, True)

        self.CheckPoint("检查点1：检查设置自动登录成功")
        user.automaticLogin(self.passwd, self.username, True)

        self.Step("步骤2:取消自动登录")
        user.setAutomaticLogin(self.passwd, self.username, False)

        self.CheckPoint("检查点2：检查取消自动登录成功")
        user.automaticLogin(self.passwd, self.username, False)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
