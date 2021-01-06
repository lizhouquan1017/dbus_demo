# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_sendAppCloseData
# @Test Description:      向数据埋点程序发送应用的关闭消息
# @Test Condition:
# @Test Step:             1.向数据埋点程序发送应用的关闭消息；
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
        self.path = self.get_data('path')
        self.name = self.get_data('name')
        self.app_id = self.get_data('app_id')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:向数据埋点程序发送应用的关闭消息并检查正常")
        userExperience.sendAppStateData(self.path, self.name, self.app_id, 'close')

    def tearDown(self):
        self.Step("收尾:")
