# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          014_setUseProxy_01
# @Test Description:      设置指定id的程序是否使用代理
# @Test Condition:        无
# @Test Step:             1.设置dde-file-manager使用代理
#                         2.检查dde-file-manager是否使用代理
#                         3.设置dde-file-manager不使用代理
# @Test Result:           2.dde-file-manager使用代理
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import setUseProxy, getUseProxy


class TestCase(OSBase):

    def setUp(self):
        self.app_id = 'dde-file-manager'
        self.target = True

    @pytest.mark.public
    def test_step(self):
        self.Step(f'步骤1:设置{self.app_id}使用代理')
        setUseProxy(self.app_id, self.target)

        self.Step(f'步骤2:检查{self.app_id}是否使用代理')
        assert getUseProxy(self.app_id)

    def tearDown(self):
        self.Step(f'步骤3:设置{self.app_id}不使用代理')
        setUseProxy(self.app_id, False)
