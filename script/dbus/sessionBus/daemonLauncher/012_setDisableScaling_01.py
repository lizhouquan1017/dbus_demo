# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          013_setDisableScaling_02
# @Test Description:      设置指定id的程序是否禁用缩放
# @Test Condition:        无
# @Test Step:             1.调用SetDisableScaling接口设置应用不禁用缩放
#                         2.调用GetDisableScaling接口查看禁用状态
#                         3.将应用程序恢复为默认状态
# @Test Result:           2.返回结果为False
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import setDisableScaling


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert setDisableScaling()

    def tearDown(self):
        setDisableScaling()
        
    

