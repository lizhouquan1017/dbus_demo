# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_getAllItemInfos.py
# @Test Description:      获取系统和当前用户所有应用程序的信息
# @Test Condition:        无
# @Test Step:             1.调用 GetAllItemInfos 函数,获取系统和当前用户所有应用程序的信息
# @Test Result:           1.获取到应用信息，且字段完整，数据类型正确
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import getAllItemInfos


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getAllItemInfos()

    def tearDown(self):
        pass
