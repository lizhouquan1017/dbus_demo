# -*- coding: utf-8 -*-
import os
import time
import logging
import datetime
from logging.handlers import RotatingFileHandler

from frame import constant


class UnionTestLogger:
    """
    主日志管理器,使用时需要主动初始化
    """
    single = False
    isinit = False

    def __new__(cls):
        """
        单例
        """
        if cls.single:
            cls.isinit = True
            return cls.single
        else:
            cls.single = super().__new__(cls)
            return cls.single

    def __init__(self, logger_file=None):
        """
        可以指定日志文件,也可默认生成
        :param logger_file: 日志文件路径
        """
        if self.isinit:
            return

        if logger_file:
            log_file_path = logger_file
        else:
            now = datetime.datetime.now()
            today_str = now.strftime('%Y_%m_%d %H_%M_%S_%f')

            date_token = today_str.split(' ')[0]
            time_token = today_str.split(' ')[1]
            log_file_name = f'{int(time.time())}.log'
            log_root_path = os.path.join(constant.root_path, 'log')
            log_file_path = os.path.join(log_root_path, date_token, time_token, log_file_name)
            if os.path.exists(log_file_path):
                pass
            else:
                os.makedirs(os.path.split(log_file_path)[0])

        main_log = logging.getLogger()
        main_log.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(name)s %(asctime)s %(levelname)s %(filename)s(%(lineno)d)::%(funcName)s - %(message)s')

        rotating_file_handler = RotatingFileHandler(log_file_path, maxBytes=10000000, encoding='utf-8')
        rotating_file_handler.setLevel(logging.DEBUG)

        rotating_file_handler.setFormatter(formatter)

        main_log.addHandler(rotating_file_handler)
