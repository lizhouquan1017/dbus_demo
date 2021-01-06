# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          008_setUpdateNotifyEnable
# @Test Description:      关闭通知更新
# @Test Condition:
# @Test Step:             1.调用 SetUpdateNotify 函数,设置关闭通知更新
# @Test Result:           1.更新提醒关闭
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import setUpdateNotify


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert setUpdateNotify(target=False)

    def tearDown(self):
        pass
