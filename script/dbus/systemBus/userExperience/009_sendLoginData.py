# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_sendLoginData
# @Test Description:      向数据埋点程序发送用户登录消息
# @Test Condition:
# @Test Step:             1.向数据埋点程序发送用户登录消息；
# @Test Result:           1.检查发送成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import userExperience


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:向数据埋点程序发送用户登录消息并检查正常")
        userExperience.sendLogonData('login')

    def tearDown(self):
        self.Step("收尾:")
