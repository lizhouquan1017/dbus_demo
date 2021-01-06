# -*- coding: utf-8 -*-

#****************************************************
# @Test Case ID:          004_setLocalRTC_04
# @Test Description:      设置实时钟为世界统一时间
# @Test Condition:
# @Test Step:             1.设置世界统一时间，不修正系统时间；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
#*****************************************************

import pytest
from frame.base import OSBase
from aw.dbus.systemBus import timedated

class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置世界统一时间，修正系统时间并检查设置成功")
        timedated.setLocalRTC(self.passwd, 'false', 'false', '')

    def tearDown(self):
        self.Step("收尾:无")
        pass