# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_isPasswordValid
# @Test Description:      查找密码是否有效
# @Test Condition:
# @Test Step:             1.输入密码进行查找；
# @Test Result:           1.查找返回状态正常;
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
        self.passwd1 = self.get_data('passwd1')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:检查密码有效")
        accounts.isPasswordValid(self.passwd, 'valid')

        # self.Step("步骤2:检查密码有无效")
        # accounts.isPasswordValid(self.passwd1,'invalid')

    def tearDown(self):
        self.Step("收尾:")
