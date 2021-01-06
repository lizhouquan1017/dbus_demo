# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_deleteGroup
# @Test Description:      用户组删除用户
# @Test Condition:        1.添加用户到用户组
# @Test Step:             1.用户组删除用户；
# @Test Result:           1.检查用户组删除用户成功;
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
        self.groupname = self.get_data('groupname')

        self.Step("预制条件2:添加用户到用户组")
        user.addGroup(self.passwd, self.username, self.groupname)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用户组删除用户")
        user.deleteGroup(self.passwd, self.username, self.groupname)

        self.CheckPoint("检查点1：检查用户组删除用户成功")
        user.checkUserGroupStatus(self.passwd, self.username, self.groupname, 'del')

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
