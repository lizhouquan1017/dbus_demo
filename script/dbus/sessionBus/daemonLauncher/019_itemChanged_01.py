# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          019_itemChanged_01
# @Test Description:      测试ItemChanged信号量
# @Test Condition:        测试机中未安装要安装的软件,若存在先卸载
# @Test Step:             1.检查使用存在vlc应用,若存在则卸载
#                         2.使用dbus-monitor命令监控com.deepin.dde.daemon.Launcher
#                         3.安装vlc
#                         4.解析dbus-monitor结果,是否监控到ItemChanged信号,判断'string "updated"'和'string "vlc"'是否在返回值中
# @Test Result:           4.监控到ItemChanged信号,'string "created"'和'string "vlc"'在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.dbus_common import root_execute_command_by_stdin
from aw.dbus.sessionBus.daemonLauncher import start_monitor_signal, stop_monitor_signal, itemChanged, is_in_apps


class TestCase(OSBase):

    def setUp(self):
        self.app = 'vlc'
        self.install_command = f'apt-get -y install {self.app}'
        self.remove_command = f'sudo apt-get -y remove {self.app}'
        self.single = 'ItemChanged'
        self.parse_flgs = ('string "created"', 'string "vlc"')
        self.passwd = self.get_data('passwd')

        self.Step(f'步骤1:检查使用存在{self.app}应用,若存在则卸载')
        if is_in_apps(self.app):
            self.Step(f'卸载{self.app}')
            logging.info(root_execute_command_by_stdin(self.remove_command, self.passwd))
            time.sleep(5)

    @pytest.mark.public
    def test_step(self):
        self.Step(f'步骤2:使用dbus-monitor命令监控com.deepin.dde.daemon.Launcher')
        dbus_monitor = start_monitor_signal(member=self.single)
        time.sleep(2)

        self.Step(f'步骤3:安装{self.app}')
        logging.info(root_execute_command_by_stdin(self.install_command, self.passwd))
        time.sleep(2)

        self.Step(
            f'''setp04:解析dbus-monitor结果,是否监控到ItemChanged信号,判断'string "created"'和'string "vlc"'是否在返回值中''')
        stop_monitor_signal(dbus_monitor)
        time.sleep(1)
        result = itemChanged(dbus_monitor, *self.parse_flgs)
        assert result

    def tearDown(self):
        self.Step(f'tearDown: 卸载{self.app}')
        logging.info(root_execute_command_by_stdin(self.remove_command, self.passwd))
        time.sleep(5)
