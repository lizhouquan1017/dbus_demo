# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          017_mirrorSource
# @Test Description:      读取当前使用的镜像源
# @Test Condition:
# @Test Step:             1.读取 MirrorSource 属性
# @Test Result:           1.返回String数据类型且值在ListMirrorSources的返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import mirrorSource


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("读取当前使用的镜像源，并检查ID是否正确")
        assert mirrorSource()

    def tearDown(self):
        pass
