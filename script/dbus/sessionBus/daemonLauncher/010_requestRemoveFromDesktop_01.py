# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          010_requestRemoveFromDesktop_01
# @Test Description:      请求将指定id的程序桌面图标删除
# @Test Condition:        桌面图标不存在桌面
# @Test Step:             1.清除应用程序桌面图标
#                         2.调用RequestRemoveFromDesktop接口,请求将指定id的程序桌面图标删除
# @Test Result:           2.报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import requestRemoveFromDesktop


class TestCase(OSBase):

    def setUp(self):
        self.app_id = 'dde-file-manager'
        self.Step(f'步骤1:删除{self.app_id}桌面图标')
        requestRemoveFromDesktop(app_id=self.app_id, ignore=True)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step(f'步骤2:调用调用RequestRemoveFromDesktop接口删除{self.app_id}桌面图标')
        assert requestRemoveFromDesktop(app_id=self.app_id, is_exists=False)
        time.sleep(2)

    def tearDown(self):
        pass
        
    

