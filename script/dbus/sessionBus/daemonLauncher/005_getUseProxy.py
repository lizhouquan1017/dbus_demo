# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_getUseProxy.py
# @Test Description:      获取id对应的程序是否使用代理,true表示使用代理，false表示不使用
# @Test Condition:
# @Test Step:             1.调用 GetUseProxy 函数,获取id对应的程序是否使用代理
# @Test Result:           1.返回正确的数据类型与数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import getUseProxy


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getUseProxy()

    def tearDown(self):
        pass
        
    

