# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_isUsernameValid
# @Test Description:      查找用户名是否有效
# @Test Condition:        1.新建一个账户
# @Test Step:             1.输入已存在账户名，进行查找；
#                         2.输入未建账户名，进行查找;
# @Test Result:           1.查找结果显示为无效账户;
#                         2.查找结果显示为有效账户;
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
        self.username1 = self.get_data('username1')

        self.Step("预制条件2:创建新账户username")
        accounts.createUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:输入已存在账户名，查找结果显示为无效账户")
        accounts.isUsernameValid(self.username, 'invalid')

        self.Step("步骤2:输入未建账户名，查找结果显示为有效账户")
        accounts.isUsernameValid(self.username1, 'valid')

    def tearDown(self):
        self.Step("收尾:删除新建账户")
        accounts.deleteUser(self.passwd, self.username)
