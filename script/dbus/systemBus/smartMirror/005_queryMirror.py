# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_queryMirror
# @Test Description:      查询最佳镜像来源
# @Test Condition:
# @Test Step:             1.查询最佳镜像来源；
# @Test Result:           1.检查查询成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import smartMirror


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.origin = self.get_data('origin')
        self.official = self.get_data('official')
        self.mirror = self.get_data('mirror')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:查询最佳镜像来源并检查成功")
        smartMirror.queryMirror(self.origin, self.official, self.mirror)

    def tearDown(self):
        self.Step("收尾:")