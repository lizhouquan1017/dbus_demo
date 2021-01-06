# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_prepare
# @Test Description:      为登录用户准备DDECGroups环境
# @Test Condition:
# @Test Step:             1.获取sessionID,运行接口；
# @Test Result:           1.检查接口运行成功;
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
        self.Step("步骤1:获取sessionID,运行接口检查运行成功")
        swapSchedhelper.checkPrepareStatus('valid')

    def tearDown(self):
        self.Step("收尾:无")
