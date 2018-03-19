import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
import configparser

# cur_path = os.path.dirname(os.path.realpath(__file__))
# configPath = os.path.join(cur_path, r"config\email.ini")

configPath = r'F:\F_lianxi\lianxi_test_ui\config\email.ini'
print(configPath)
conf = configparser.ConfigParser()
conf.read(configPath, encoding='UTF-8')

my_sender = conf.get('email', 'smtp_server')
my_pass = conf.get('email', 'psw')
server = conf.get('email', 'smtp_server')
port = conf.get('email', 'port')
my_user = conf.get('email', 'receiver')

  # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("command not implemented'command not implemented'", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception as msg:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
        print(str(msg))
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")