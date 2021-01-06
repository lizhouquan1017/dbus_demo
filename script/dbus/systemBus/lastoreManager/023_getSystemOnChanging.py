# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          023_getSystemOnChanging
# @Test Description:      是否正在更新中
# @Test Condition:
# @Test Step:             1.获取是否正在更新中；
# @Test Result:           1.检查操作成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import lastoreManager


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取可以升级的软件信息,并检查操作成功")
        lastoreManager.systemOnChanging()

    def tearDown(self):
        self.Step("收尾:无")
