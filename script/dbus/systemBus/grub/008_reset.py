# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_reset
# @Test Description:      重置所有的设置
# @Test Condition:
# @Test Step:             1.重置所有的设置；
#
# @Test Result:           1.检查重置所有的设置成功;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import grub


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

        self.Step("预制条件2:重置所有设置")
        grub.reset(self.passwd)

        self.Step("检查点2:检查grub主题已默认开启")
        grub.checkThemeStatus('enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置关闭grub主题")
        grub.setEnableTheme(self.passwd, 'disable')

        self.CheckPoint("检查点1：检查关闭主题成功")
        grub.checkThemeStatus('disable')

        self.Step("步骤2:重置所有设置")
        grub.reset(self.passwd)

        self.Step("检查点2.1:检查grub主题已开启")
        grub.checkThemeStatus('enable')

        self.Step("检查点2.2:检查获取主题文件成功")
        grub.getThemeFile()

    def tearDown(self):
        self.Step("收尾:恢复默认背景")
        grub.setEnableTheme(self.passwd, 'disable')
        grub.setEnableTheme(self.passwd, 'enable')
