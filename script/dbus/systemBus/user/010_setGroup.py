# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_setGroup
# @Test Description:
# @Test Condition:
# @Test Step:             1.添加用户附加群组1和2；
# @Test Result:           1.检查添加用户附加群组成功;
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
        self.groupname1 = self.get_data('groupname1')
        self.groupname2 = self.get_data('groupname2')

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:添加用户附加群组")
        user.setGroups(self.passwd, self.username, self.groupname1, self.groupname2)

        self.CheckPoint("检查点1：检查添加用户附加群组成功")
        user.checkSetGroups(self.passwd, self.username, self.groupname1, self.groupname2)

    def tearDown(self):
        self.Step("收尾:")
        user.delete_group(self.passwd, self.groupname1)
        user.delete_group(self.passwd, self.groupname2)
        accounts.deleteUser(self.passwd, self.username)
