# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_disableNoPasswdLogin
# @Test Description:      取消无密码登陆
# @Test Condition:
# @Test Step:             1.设置取消无密码登陆；
# @Test Result:           1.检查设置取消无密码登陆;
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

        self.Step("预制条件1:设置无需密码登陆")
        user.enableNoPasswdLogin(self.passwd, self.username, 'enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置需密码登")
        user.enableNoPasswdLogin(self.passwd, self.username, 'disable')

        self.CheckPoint("检查点1：检查设置需密码登成功")
        user.checkNoPasswdLoginStatus(self.passwd, self.username, 'disable')

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
