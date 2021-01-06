# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_listMirrorSources
# @Test Description:      是否可以获取镜像源
# @Test Condition:
# @Test Step:             1.调用 ListMirrorSources 函数,获取系统和当前用户所有应用程序的信息
# @Test Result:           1.可以获取到默认镜像源
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import listMirrorSources


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert listMirrorSources()

    def tearDown(self):
        pass
