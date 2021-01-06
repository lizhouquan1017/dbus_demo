# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getDisableStatus
# @Test Description:      获取非使能标志状态
# @Test Condition:
# @Test Step:             1.设置关闭智能选择镜像；
# @Test Result:           1.检查获取非使能标志成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import smartMirror


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:设置关闭智能选择镜像")
        smartMirror.setEnable('disable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:检查设置打开智能选择镜像")
        smartMirror.getEnableStatus()

    def tearDown(self):
        self.Step("收尾:")
