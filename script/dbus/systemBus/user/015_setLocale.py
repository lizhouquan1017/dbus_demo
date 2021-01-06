# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_setHomeDir
# @Test Description:
# @Test Condition:
# @Test Step:             1.设置本地化信息；
# @Test Result:           1.检查设置本地化信息成功;
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
        self.local_info = self.get_data('local_info')

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置本地化信息")
        user.setLocale(self.passwd, self.username, self.local_info)

        self.CheckPoint("检查点1：检查设置本地化信息成功")
        user.checksetLocaleStatus(self.passwd, self.username, self.local_info)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
