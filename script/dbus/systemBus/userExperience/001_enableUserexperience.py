# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_enableUserexperience
# @Test Description:      打开用户体验计划
# @Test Condition:
# @Test Step:             1.打开用户体验计划；
# @Test Result:           1.检查打开用户体验计划成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import userExperience


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        userExperience.enableUserexperience('disable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:打开用户体验计划")
        userExperience.enableUserexperience('enable')

        self.CheckPoint("检查点1：检查打开用户体验成功")
        userExperience.checkEnableUserexperience('enable')

    def tearDown(self):
        self.Step("收尾:关闭用户体验计划")
        userExperience.enableUserexperience('disable')
