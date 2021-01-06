# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_getDisableScaling
# @Test Description:      获取id对应的程序是否禁用缩放,true表示禁用，false表示不禁用
# @Test Condition:
# @Test Step:             1.调用 GetDisableScaling 函数,获取id对应的程序是否禁用缩放
# @Test Result:           1.返回正确的数据类型与数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import getDisableScaling


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getDisableScaling()

    def tearDown(self):
        pass
