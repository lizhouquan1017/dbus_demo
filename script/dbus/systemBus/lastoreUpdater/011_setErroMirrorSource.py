# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          011_setErroMirrorSource
# @Test Description:      设置错误的MirrorSourceID
# @Test Condition:
# @Test Step:             1.调用 SetMirrorSource 函数,设置一个不存在的源ID
# @Test Result:           1.设置不成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import setErrorMirrorSource, setMirrorSource


class TestCase(OSBase):

    def setUp(self):
        self.passwd = self.get_data('passwd')

    @pytest.mark.public
    def test_step(self):
        self.Step("传入错误的id，预期设置不成功")
        assert setErrorMirrorSource(self.passwd, source_id='dddddd')

    def tearDown(self):
        setMirrorSource(self.passwd, 'default')
