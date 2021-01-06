# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          034_deleteIconFile
# @Test Description:
# @Test Condition:
# @Test Step:             1.删除不是用户当前图标的自定义图标；
# @Test Result:           1.删除不是用户当前图标的自定义图标成功;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:删除不是用户当前图标的自定义图标且检查成功")
        user.deleteIconFile(self.passwd, self.username)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
