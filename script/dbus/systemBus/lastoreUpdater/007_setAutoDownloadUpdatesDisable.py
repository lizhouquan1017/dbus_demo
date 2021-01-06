# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_setAutoDownloadUpdatesDisable
# @Test Description:      设置不自动下载更新
# @Test Condition:
# @Test Step:             1.调用 SetAutoDownloadUpdates 函数,设置关闭自动下载更新
# @Test Result:           1.自动下载更新关闭
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
        assert setAutoDownloadUpdates(target=False)

    def tearDown(self):
        pass
