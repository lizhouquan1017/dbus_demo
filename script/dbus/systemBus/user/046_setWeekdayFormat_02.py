# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          046_setWeekdayFormat_02
# @Test Description:      设置星期格式
# @Test Condition:
# @Test Step:             1.设置星期格式为1表示 周一；
# @Test Result:           1.检查设置成功;
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
        self.value = 1

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:设置星期格式为1表示 周一")
        user.setWeekdayFormat(self.passwd, self.username, self.value)

        self.CheckPoint("检查点1：检查设置成功")
        user.checkSetWeekdayFormat(self.passwd, self.username, self.value)

    def tearDown(self):
        self.Step("收尾:删除测试账户")
        accounts.deleteUser(self.passwd, self.username)
