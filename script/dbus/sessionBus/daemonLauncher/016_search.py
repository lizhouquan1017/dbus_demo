# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          016_search
# @Test Description:      开始菜单中搜索应用程序
# @Test Condition:        无
# @Test Step:             1.使用dbus-monitor命令监控com.deepin.dde.daemon.Launcher
#                         2.调用接口搜索dde-file-manager
#                         3.解析dbus-monitor结果,是否监控到SearchDone信号,判断'string "dde-file-manager"'是否在返回值中
# @Test Result:           3.监控到SearchDone信号,'string "dde-file-manager"'在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import start_monitor_signal, stop_monitor_signal, search, searchDone


class TestCase(OSBase):

    def setUp(self):
        self.single = 'SearchDone'
        self.parse_flg = 'string "dde-file-manager"'

    @pytest.mark.public
    def test_step(self):
        self.Step(f'步骤1:使用dbus-monitor命令监控com.deepin.dde.daemon.Launcher')
        dbus_monitor = start_monitor_signal(member=self.single)
        time.sleep(2)

        self.Step(f'步骤2:调用接口搜索dde-file-manager')
        search()
        time.sleep(2)

        self.Step(f'''步骤3:解析dbus-monitor结果，是否监控到SearchDone信号，判断'string "dde-file-manager"'是否在返回值中''')
        stop_monitor_signal(dbus_monitor)
        time.sleep(1)
        result = searchDone(dbus_monitor, self.parse_flg)
        assert result

    def tearDown(self):
        pass
