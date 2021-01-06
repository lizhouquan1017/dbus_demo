# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_setAutoCheckUpdatesEnable
# @Test Description:      设置自动检查更新
# @Test Condition:
# @Test Step:             1.调用 SetAutoCheckUpdates 函数,设置开启自动检查更新
# @Test Result:           1.开启自动检查更新
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import setAutoCheckUpdates


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert setAutoCheckUpdates(target=True)

    def tearDown(self):
        pass
