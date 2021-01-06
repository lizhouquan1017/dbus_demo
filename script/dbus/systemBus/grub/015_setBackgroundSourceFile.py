# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_setBackgroundSourceFile
# @Test Description:      设置GRUB引导菜单的背景文件的绝对路径
# @Test Condition:        1.设置filename1为背景文件，文件大小为11M
# @Test Step:             1.设置filename2为GRUB引导菜单的背景文件；
#
# @Test Result:           1.检查设置filename2为背景文件成功;
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
        self.filename1 = self.get_data('filename1')
        self.filename2 = self.get_data('filename2')

        self.Step("预制条件2:设置filename1为背景文件")
        grub.setBackgroundSourceFile(self.passwd, self.filename1)
        grub.getBackgroundSourceFileSize()

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置filename2为背景文件")
        grub.setBackgroundSourceFile(self.passwd, self.filename2)

        self.CheckPoint("检查点1:检查设置filename2为背景文件成功")
        grub.checkSetBackgroundSourceFile()

    def tearDown(self):
        self.Step("收尾:设置filename1为背景文件")
        grub.setBackgroundSourceFile(self.passwd, self.filename1)
        grub.getBackgroundSourceFileSize()
