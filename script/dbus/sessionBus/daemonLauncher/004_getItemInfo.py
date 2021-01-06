# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_getItemInfo.py
# @Test Description:      获取id对应的程序的详细信息
# @Test Condition:
# @Test Step:             1.调用 GetItemInfo 函数,获取id对应的程序的详细信息
# @Test Result:           1.返回正确的数据类型
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import getItemInfo


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getItemInfo()

    def tearDown(self):
        pass
        
    

