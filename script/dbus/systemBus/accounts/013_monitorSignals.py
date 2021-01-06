# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_monitorSignals
# @Test Description:      监控account信号
# @Test Condition:
# @Test Step:             1.分别增加和删除用户，触发信号接收；
#
# @Test Result:           1.检查分别接收到增加和删除用户的信号提示;
#
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
        self.Step("步骤1:分别增加和删除用户，触发信号接收并检查信号接收成功")
        accounts.monitorSignals(self.passwd, self.username)

    def tearDown(self):
        self.Step("收尾:")
