# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_isEnabledUserexperience
# @Test Description:      返回用户体验计划是否打开
# @Test Condition:
# @Test Step:             1.返回用户体验计划是否打开；
# @Test Result:           1.检查返回成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import userExperience


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:打开用户体验计划")
        userExperience.enableUserexperience('enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:返回用户体验计划是否打开")
        userExperience.isEnabled()

        self.CheckPoint("检查点1：检查返回成功")
        userExperience.checkIsEnabled()

    def tearDown(self):
        self.Step("收尾:关闭用户体验计划")
        userExperience.enableUserexperience('disable')
