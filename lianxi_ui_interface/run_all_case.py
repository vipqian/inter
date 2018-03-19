# coding=utf-8
"""
author:
date:
brief:  运行全部测试用例
"""

import os
import unittest
from lianxi_ui_interface.common.HTMLTestRunner_jpg import HTMLTestRunner
import time
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import configparser
from email.utils import formataddr


def add_case():
    """
    添加报告路径，添加所有的测试用例
    :return: 一个包含路径下所有测试用例（test*.py）的list集合
    """
    testunit = unittest.TestSuite()
    case_path = os.path.join(os.getcwd(), 'case')
    print("测试用例的路径 %s" % case_path)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    testunit.addTests(discover)
    # print(testunit)
    return testunit


def report_path():
    """报告路径"""
    result_path = os.path.join(os.getcwd(), 'report')
    if os.path.isdir(result_path):
        pass
    else:
        os.makedirs(result_path)
    return result_path


def run_case():
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    result_abspath = os.path.join(report_path(), ('%s.html' % now))
    print(result_abspath)
    fp = open(result_abspath, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title="自动化测试",
    #                                        description="用例执行情况")
    runner = HTMLTestRunner(title="自动化测试报告",
                            description="用例执行情况",
                            stream=fp,
                            retry=0,
                            )
    runner.run(add_case())
    fp.close()


def get_report_file():
    lists = os.listdir(report_path())
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path(), fn)))
    report_file = lists[-1]
    print("最新的测试的报告为：%s" % report_file)
    return os.path.join(report_path(), report_file)


def send_mail():
    """
    发送最新的测试报告
    :return:
    """
    cur_path = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(cur_path, r"config\email.ini")
    conf = configparser.ConfigParser()
    conf.read(configPath, encoding='UTF-8')

    sender = conf.get('email', 'sender')
    pwd = conf.get('email', 'psw')
    server = conf.get('email', 'smtp_server')
    port = conf.get('email', 'port')
    receiver = conf.get('email', 'receiver')
    # receiver = receiver.split(',')


    time.sleep(2)
    report_file = get_report_file()
    with open(report_file, 'rb') as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = '自动化测试报告'
    msg['from'] = sender
    msg['to'] = receiver
    #添加时间
    msg['date'] = time.strftime('%a,%d,%b,%Y_%M_%S %Z')
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "report.html"'
    msg.attach(att)
    #发件人邮箱中的SMTP服务器，端口是465
    smtp = smtplib.SMTP_SSL(server, port)

    # 登录用户名和密码
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver.split(','), msg.as_string())
    smtp.quit()
    print('邮件已经发送给：%s' % str(receiver))


if __name__ == '__main__':
    # add_case()
    run_case()
    # send_mail()
