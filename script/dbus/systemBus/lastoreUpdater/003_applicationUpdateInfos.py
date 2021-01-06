# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_applicationUpdateInfos
# @Test Description:      获取应用程序更新信息
# @Test Condition:
# @Test Step:             1.调用 ApplicationUpdateInfos 函数,获取应用程序更新信息,对应应用商店->应用更新中的信息
# @Test Result:           1.在应用商店中若存在需要更新的软件，则返回的Array中包含软件信息
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import applicationUpdateInfos


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert applicationUpdateInfos()

    def tearDown(self):
        pass
