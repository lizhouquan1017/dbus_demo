#-*- coding:utf-8 -*-
import unittest
import importlib
import HTMLReport
import time
import sys
import logging
from frame import constant,sendemail
from frame.common import get_case

def exc_case():
    case=get_case()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for item in case:
        params=importlib.import_module(item) 
        suite.addTest(loader.loadTestsFromTestCase(params.testCase))
    runner = HTMLReport.TestRunner(title="测试报告",
                                   report_file_name="test" + constant.time_,
                                   output_path=constant.report_path,
                                   lang="cn")
    runner.run(suite)

if __name__=="__main__":
    common = sys.argv
    exc_case()
    if 2 == len(common):
        if 'email' == sys.argv[1]:
            sendemail.sendEmail()
    else:
        logging.info("调试程序，无需发送邮件！")








