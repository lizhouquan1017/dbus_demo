# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_setHistoryLayout
# @Test Description:
# @Test Condition:
# @Test Step:             1.设置历史布局；
# @Test Result:           1.检查设置历史布局成功;
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
        self.layout1 = self.get_data('layout1')
        self.layout2 = self.get_data('layout2')

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置用户头像")
        user.setHistoryLayout(self.passwd, self.username, self.layout1, self.layout2)

        self.CheckPoint("检查点1：检查设置用户头像成功")
        user.checkSetHistoryLayout(self.passwd, self.username, self.layout1, self.layout2)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
