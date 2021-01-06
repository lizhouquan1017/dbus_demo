# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_randUserIcons
# @Test Description:      随机返回一个用户头像的文件绝对路径
# @Test Condition:
# @Test Step:             1.执行randUserIcons接口；
#
# @Test Result:           1.随机返回一个用户头像的文件绝对路径;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:执行randUserIcons接口，检查输出为户头像的文件绝对路径")
        accounts.randUserIcon()

    def tearDown(self):
        self.Step("收尾:")
