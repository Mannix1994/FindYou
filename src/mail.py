# -*- coding: UTF-8 -*-

import smtplib
import email.mime.multipart
import email.mime.text


def send_email(content):
    """
    发送邮件
    :param content: 邮件内容
    :return: 空
    """
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "13281286897@163.com"  # 用户名
    mail_pass = "qazwsx123"  # 口令

    sender = mail_user
    receiver = '2311136142@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msg = email.mime.multipart.MIMEMultipart()
    ''''' 
    最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因 
    '''
    msg['Subject'] = '发现符合条件的女子'
    msg['From'] = sender
    msg['To'] = receiver

    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp_server = smtplib.SMTP()
    smtp_server.connect(mail_host, '25')
    smtp_server.login(mail_user, mail_pass)
    smtp_server.sendmail(mail_user, receiver, msg.as_string())
    smtp_server.quit()
    print('邮件发送成功')


if __name__ == "__main__":
    content = '''
           你好，xiaoming
           这是一封自动发送的邮件。
           www.ustchacker.com
       '''
    # send_email(content)
    print(len(content.split('m'))-1)

