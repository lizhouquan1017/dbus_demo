# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_setLocked
# @Test Description:      锁定/解锁用户密码
# @Test Condition:
# @Test Step:             1.锁定用户；
#                         2.解锁用户；
# @Test Result:           1.检查锁定用户成功;
#                         2.检查解锁用户成功;
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

        self.Step("预制条件3:设置账户密码")
        user.setPassword(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置锁定用户")
        user.setLocked(self.passwd, self.username, 'lock')

        self.CheckPoint("检查点1：检查锁定用户成功")
        user.locked(self.passwd, self.username, 'lock')

        self.Step("步骤2:设置解锁用户")
        user.setLocked(self.passwd, self.username, 'unlock')

        self.CheckPoint("检查点2：检查解锁用户成功")
        user.locked(self.passwd, self.username, 'unlock')

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
