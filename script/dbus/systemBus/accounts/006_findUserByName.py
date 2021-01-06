# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_findUserByName
# @Test Description:      根据用户名称查找用户账户
# @Test Condition:
# @Test Step:             1.根据用户名称查找用户账户；
# @Test Result:           1.检查查找账户成功;
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
        self.Step("步骤1:新建账户，根据新建账户名称查找账户,并检查查找成功")
        accounts.findUserByName(self.passwd, self.username)

    def tearDown(self):
        self.Step("收尾:删除新建账户")
        accounts.deleteUser(self.passwd, self.username)
