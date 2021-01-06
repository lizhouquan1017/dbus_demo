# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_prepare_02
# @Test Description:      为登录用户准备DDECGroups环境
# @Test Condition:
# @Test Step:             1.输入无效的sessionID，运行接口；
# @Test Result:           1.获取sessions报错，信息为：not found session;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import swapSchedhelper


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:输入无效sessionID,检查接口报错信息正确")
        swapSchedhelper.checkPrepareStatus('invalid')

    def tearDown(self):
        self.Step("收尾:无")
