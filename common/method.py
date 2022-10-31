# -*- coding:utf-8 -*-
# user:Liukang
import time
import HTMLTestRunner
import os.path
from email.mime.text import MIMEText
from email.header import Header
import smtplib

class Method(object):
    def __init__(self, driver):
        self.driver = driver
    # 邮件发送最新HTML测试报告
    def report_email(suite, title):
        # 生成HTMLRunner测试报告
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        filename = os.path.dirname(os.path.dirname(__file__)) + '/test_report/'
        #——————————————————————————————————————此处修改报告名——————————————————————————————————————————
        HtmlFile = filename + now + '.html'
        fp = open(HtmlFile, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=title,description=u"用例执行情况")
        try:
            runner.run(suite)
            fp.close()
            print("报告已生成：%s" % HtmlFile)

            # 获取最新报告
            try:
                lists = os.listdir(filename)
                lists.sort(key=lambda fn: os.path.getatime(filename + "\\" + fn))
                file_new = os.path.join(filename, lists[-1])
                print("已获取最新测试报告：" + file_new)
                # 发送邮件
                try:
                    f = open(file_new, 'rb')
                    mail_bady = f.read()
                    f.close()

                    msg = MIMEText(mail_bady, 'html', 'utf-8')
                    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
                    msg['Subject'] = Header("自动化测试报告" + rq, 'utf-8')

                    try:
                        smtp = smtplib.SMTP()
                        smtp.connect("smtp.qq.com")
                        smtp.login("1661289226@qq.com", "fztwjhnxyveydgad")
                        smtp.sendmail("1661289226@qq.com", "1445034070@qq.com", msg.as_string())
                        smtp.quit()
                        print('自动化测试报告发送成功 !')
                    except Exception as e:
                        print("测试报告发送失败 ！" + e)
                        return e
                except Exception as e:
                    print(e)
                    return e
            except Exception as e:
                print("最新报告获取失败 ！" + e)
                return e
        except Exception as e:
            print("报告生成失败 ！" + e)
            return e

