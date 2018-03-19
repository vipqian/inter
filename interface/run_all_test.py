# coding=utf-8
"""
author:
date:
brief: 执行所有测试用例
"""

import os
import smtplib
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.HTMLTestRunner_jpg import HTMLTestRunner
from config import readConfig

# 当前脚本的真是路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName = "case", rule = "test*.py"):
    """用discover方法加载所有的测试用例"""
    case_path = os.path.join(cur_path, caseName)        #用例文件夹
    # 如果不存在就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)

    # 定义discover方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)

    # print(discover)
    return discover


def run_case(all_case, reportNanme="report"):
    """执行所有的测试用例并且生成HTML测试报告"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportNanme)
    # 如果不存在就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    print("report path is: %s" % report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=fp, title="自动化测试报告，测试结果如下：", description="用例执行情况：", retry=0)

    # 调用add_case函数
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    "获取最新的测试报告"
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print("最新的测试报告： " + lists[-1])
    # 找到最新的测试报告
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    """发送最新的的测试报告内容"""
    with open(report_file, 'rb') as f:
        mail_body = f.read()


    # 定义邮件内容
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u"自动化测试报告"
        msg["from"] = sender
        msg["to"] = psw
        msg.attach(body)
        # 添加附件
        att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)
        try:
            smtp = smtplib.SMTP_SSL(smtpserver, port)
        except:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, port)
        # 用户名密码
        smtp.login(sender, psw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')
if __name__ == "__main__":
    all_case = add_case()   # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)        # 2执行用例
    # 获取最新的测试报告文件
    # report_path = os.path.join(cur_path, "report")  # 用例文件夹
    # report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # #邮箱配置
    # sender = readConfig.sender
    # psw = readConfig.psw
    # smtp_server = readConfig.smtp_server
    # port = readConfig.port
    # receiver = readConfig.receiver
    # send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告