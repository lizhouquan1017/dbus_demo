# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_statusSaved
# @Test Description:      StatusSaved (string, string, bool)
#                         标记某个应用是否启动过的状态文件被保存的信号
#                         第一个参数为应用的desktopFile文件目录，第二个为标记记录配置文件，第三个为是否标记成功
# @Test Condition:        无
# @Test Step:             1.安装 vlc 应用
#                         2.使用 dbus-monitor 命令监控com.deepin.daemon.Apps.LaunchedRecorder
#                         3.卸载 vlc 应用
#                         4.解析 dbus-monitor 结果,是否监控到 StatusSaved 信号,判断'string "/usr/share/applications"是否在返回值中
# @Test Result:           4.监控到 StatusSaved 信号,'string "/usr/share/applications”在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import appsLaunchedRecorder
from aw.dbus.dbus_common import root_execute_command_by_stdin, start_monitor_signal_for_system, stop_monitor_signal


class TestCase(OSBase):
    def setUp(self):
        self.app = 'vlc'
        self.install_command = f'apt-get -y install {self.app}'
        self.remove_command = f'sudo apt-get -y remove {self.app}'
        self.single = 'StatusSaved'
        self.parse_flgs = ('string "/usr/share/applications"',)
        self.passwd = self.get_data('passwd')

        self.Step(f'步骤1:安装{self.app}')
        logging.info(root_execute_command_by_stdin(self.install_command, self.passwd))
        time.sleep(5)

        self.Step(f"步骤2:使用dbus-monitor命令监控com.deepin.daemon.Apps.LaunchedRecorder")
        self.dbus_monitor = start_monitor_signal_for_system(appsLaunchedRecorder.IFACE_NAME,
                                                            appsLaunchedRecorder.DBUS_PATH,
                                                            member=self.single)
        time.sleep(5)

    @pytest.mark.public
    def test_step(self):
        self.Step(f"步骤2:卸载{self.app}应用")
        logging.info(root_execute_command_by_stdin(self.remove_command, self.passwd))
        time.sleep(5)
        appsLaunchedRecorder.statusSaved(self.dbus_monitor, *self.parse_flgs)

    def tearDown(self):
        self.Step("收尾:stop_monitor_signal")
        stop_monitor_signal(self.dbus_monitor)
        time.sleep(2)

    

