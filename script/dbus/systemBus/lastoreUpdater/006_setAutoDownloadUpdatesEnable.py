# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_setAutoDownloadUpdatesEnable
# @Test Description:      设置自动下载更新
# @Test Condition:
# @Test Step:             1.调用 SetAutoDownloadUpdates 函数,设置开启自动下载更新
# @Test Result:           1.自动下载更新开启
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import setAutoDownloadUpdates


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert setAutoDownloadUpdates(target=True)

    def tearDown(self):
        pass
