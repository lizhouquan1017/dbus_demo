# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_isItemOnDesktop_01
# @Test Description:      获取id对应的程序是否有桌面图标,true表示桌面有图标，false表示没有
# @Test Condition:        桌面图标存在桌面
# @Test Step:             1.创建桌面图标
#                         2.调用IsItemOnDesktop接口,获取id对应的程序是否有桌面图标
#                         3.移除桌面图标
# @Test Result:           2.返回true
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import requestSendToDesktop, isItemOnDesktop, requestRemoveFromDesktop


class TestCase(OSBase):

    def setUp(self):
        self.app_id = 'dde-file-manager'
        self.Step(f'步骤1:创建{self.app_id}桌面图标')
        requestSendToDesktop(app_id=self.app_id, ignore=True)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.CheckPoint(f'步骤2:检查{self.app_id}桌面图标是否存在')
        assert isItemOnDesktop(app_id=self.app_id, target=True)
        time.sleep(2)

    def tearDown(self):
        self.Step(f'步骤2:删除{self.app_id}桌面图标')
        requestRemoveFromDesktop(app_id=self.app_id, ignore=True)
        time.sleep(2)
