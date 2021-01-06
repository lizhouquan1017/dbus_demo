# -*- coding: utf-8 -*-
import logging
import dbus

from aw.dbus.dbus_common import get_session_dbus_interface
from aw.dbus.sessionBus import sessionCommon
from frame.decorator import checkword

DBUS_NAME = 'com.deepin.SessionManager'
DBUS_PATH = '/com/deepin/SessionManager'
IFACE_NAME = 'com.deepin.SessionManager'


def dbus_interface():
    return get_session_dbus_interface(DBUS_NAME, DBUS_PATH, IFACE_NAME)


@checkword
def allowSessionDaemonRun():
    """
    相当于SessionManger的allowSessionDaemonRun字段的Get方法, 获得allowSessionDaemonRun的值
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.AllowSessionDaemonRun()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def canHibernate():
    """
    对Login1.Manager.CanHibernate进行封装, 测试系统是否支持休眠。
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.CanHibernate()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def canLogout():
    """
    返回是否能注销，目前恒为true
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.CanLogout()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def canReboot():
    """
    通过调用Login1.Manager.CanReboot(0)测试是否能重启
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.CanReboot()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def canShutdown():
    """
    通过调用Login1.Manager.CanPoweroff(0) 测试是否能关机
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.CanShutdown()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def canSuspend():
    """
    根据是否有文件/sys/power/mem_sleep 判断是否能待机，如有 根据Login1.Manager.CanSuspend 测试是否能待机
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.CanSuspend()
    if isinstance(result, dbus.Boolean):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Boolean:{type(result)}')
        return False


@checkword
def getInhibitors():
    """
    遍历得到 Inhibitor 的路径列表，Inhibitor 是操作拦截器的意思，可以阻止一些由 flags 指定的操作
    :return: True or False
    """
    interface = dbus_interface()
    result = interface.GetInhibitors()
    if isinstance(result, dbus.Array):
        logging.info(result)
        return True
    else:
        logging.info(f'返回数据不是Array:{type(result)}')
        return False
