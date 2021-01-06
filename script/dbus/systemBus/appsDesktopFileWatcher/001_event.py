# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_event
# @Test Description:      Event (string, uint32)
#                         服务监视的目录如果有文件新增或者删除，会触发该信号
#                         第一个参数为新增或者删除的文件绝对路径字符串
#                         第二个参数为0
# @Test Condition:        无
# @Test Step:             1.安装vlc应用
#                         2.使用dbus-monitor命令监控com.deepin.daemon.Apps.DesktopFileWatcher
#                         3.卸载vlc应用
#                         4.解析dbus-monitor结果,是否监控到Event信号,判断'string "/usr/share/applications是否在返回值中
# @Test Result:           4.监控到Event信号,'string "/usr/share/applications在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import appsDesktopFileWatcher
from aw.dbus.dbus_common import root_execute_command_by_stdin, start_monitor_signal_for_system, stop_monitor_signal


class TestCase(OSBase):
    def setUp(self):
        self.app = 'vlc'
        self.install_command = f'apt-get -y install {self.app}'
        self.remove_command = f'sudo apt-get -y remove {self.app}'
        self.single = 'Event'
        self.parse_flgs = ('string "/usr/share/applications',)
        self.passwd = self.get_data('passwd')

        self.Step(f'步骤1:安装{self.app}')
        logging.info(root_execute_command_by_stdin(self.install_command, self.passwd))
        time.sleep(5)

        self.Step(f"步骤2:使用dbus-monitor命令监控com.deepin.daemon.Apps.DesktopFileWatcher")
        self.dbus_monitor = start_monitor_signal_for_system(appsDesktopFileWatcher.IFACE_NAME,
                                                            appsDesktopFileWatcher.DBUS_PATH,
                                                            member=self.single)
        time.sleep(5)

    @pytest.mark.public
    def test_step(self):
        self.Step(f"步骤2:卸载{self.app}应用")
        logging.info(root_execute_command_by_stdin(self.remove_command, self.passwd))
        time.sleep(5)
        appsDesktopFileWatcher.event(self.dbus_monitor, *self.parse_flgs)

    def tearDown(self):
        self.Step("收尾:stop_monitor_signal")
        stop_monitor_signal(self.dbus_monitor)
        time.sleep(2)
