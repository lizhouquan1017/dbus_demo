# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_getNTPServer
# @Test Description:      获取网络时间协议服务器
# @Test Condition:
# @Test Step:             1.获取网络时间协议服务器；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import timedated


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

        self.Step("预制条件2:设置时区")
        timedated.setTimezone(self.passwd, 'Asia/Shanghai', '')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取网络时间协议服务器参数成功")
        timedated.getNTPServer()

    def tearDown(self):
        self.Step("收尾:无")
