# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_enableSmartmirror
# @Test Description:      设置打开智能选择镜像
# @Test Condition:
# @Test Step:             1.设置打开智能选择镜像；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import smartMirror


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置打开智能选择镜像")
        smartMirror.setEnable('enable')

        self.CheckPoint("检查点1：检查设置成功")
        smartMirror.checkSmartmirrorStatus('enable')

    def tearDown(self):
        self.Step("收尾:关闭智能选择镜像")
        smartMirror.setEnable('disable')
