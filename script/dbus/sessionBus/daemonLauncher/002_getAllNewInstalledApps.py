# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_getAllNewInstalledApps.py
# @Test Description:      获取最近新安装的app列表
# @Test Condition:
# @Test Step:             1.调用 GetAllNewInstalledApps 函数,获取最近新安装的app列表
# @Test Result:           1.返回正确的数据类型
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import getAllNewInstalledApps


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getAllNewInstalledApps()

    def tearDown(self):
        pass
