# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          022_setType
# @Test Description:      用于根据资源类型设置当前资源.
# @Test Condition:        无
# @Test Step:             1.调用Set函数，用于根据资源类型设置当前资源；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.resource = "cursor"
        self.name = "bloom-dark"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于根据资源类型设置当前资源")
        appearance.setType(self.resource, self.name)

    def tearDown(self):
        self.Step("收尾:无")
