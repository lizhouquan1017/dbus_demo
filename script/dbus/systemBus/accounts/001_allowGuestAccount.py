# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_allowGuestAccount
# @Test Description:      设置是否允许来宾账户
# @Test Condition:
# @Test Step:             1.分别设置为允许和不允许；
# @Test Result:           1.检查参数是否设置成功;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置允许来宾账户")
        accounts.allowGuestAccount(self.passwd, 'enable')

        self.CheckPoint("检查点1：检查设置允许来宾账户成功")
        accounts.getAllowGuestStatus('enable')

        self.Step("步骤2:设置不允许来宾账户")
        accounts.allowGuestAccount(self.passwd, 'disable')

        self.CheckPoint("检查点2：检查设置不允许来宾账户成功")
        accounts.getAllowGuestStatus('disable')

    def tearDown(self):
        self.Step("收尾:设置允许来宾账户")
        accounts.allowGuestAccount(self.passwd, 'enable')
