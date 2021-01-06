# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_setFullName
# @Test Description:
# @Test Condition:
# @Test Step:             1.修改用户名；
# @Test Result:           1.检查修改用户名成功;
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
        self.test_name = self.get_data('test_name')

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置自动登录")
        user.setFullName(self.passwd, self.username, self.test_name)

        self.CheckPoint("检查点1：检查设置自动登录成功")
        user.fullName(self.passwd, self.username, self.test_name)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
