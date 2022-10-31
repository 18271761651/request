# -*- coding:utf-8 -*-
# user:Liukang

import smtplib
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = '1661289226@qq.com'        #发送邮件
receiver = '1445034070@qq.com'      #接收邮件
subject = '自动化测试报告'             #发送邮件主题
smtpserver = 'smtp.qq.com'          #发送邮件服务器
username = sender                   #发送邮件用户
password = 'fztwjhnxyveydgad'       #发送邮件授权码
#获取test_report目录下的目标文件
#------------------------------------------发送文件----------------------------------------
OBJ='2021-03-28-14-24-00.html'        #文件名
file_path = os.path.dirname(os.path.abspath('.')) + '/test_report/{}'.format(OBJ)
sendfile = open(file_path, 'rb').read()
#编写邮件正文
att = MIMEText(sendfile, 'base64', 'utf-8')		#引入附件
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment;filename='{}'".format(OBJ)

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
