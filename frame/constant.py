# -*- coding:utf-8 -*-
import os
import time

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

time_ = time.strftime('%Y_%m_%d_%H_%M_%S')
# dir_name = os.path.join(os.path.join(root_path, 'report'))
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# report_path = os.path.join(os.path.join(dir_name, time_))
resoure_path = os.path.join(os.path.join(root_path, 'resource'))
dbus_path = os.path.join(os.path.join(resoure_path, 'dbus'))
deb_path = os.path.join(os.path.join(resoure_path, 'deb'))

if not os.path.exists(dbus_path):
    os.mkdir(dbus_path)
