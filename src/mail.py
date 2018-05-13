# -*- coding: UTF-8 -*-

import smtplib
import email.mime.multipart
import email.mime.text

# 这里需要导入自己的信息
try:
    # from config import my_email_config
    from config_backup import my_email_config
except ImportError:
    # from .config import my_email_config
    from .config_backup import my_email_config


def send_email(mail_subject, mail_content):
    """
    发送邮件
    :param mail_subject 邮件主题
    :param mail_content: 邮件内容
    :return: 空
    """
    # 第三方 SMTP 服务，推荐163
    host = my_email_config['host']  # 设置服务器
    sender = my_email_config['sender']  # 用户名
    password = my_email_config['password']  # 口令
    receiver = my_email_config['receiver']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msg = email.mime.multipart.MIMEMultipart()

    '''
    邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因 
    '''
    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = receiver

    txt = email.mime.text.MIMEText(mail_content)
    msg.attach(txt)

    smtp_server = smtplib.SMTP()
    smtp_server.connect(host, '25')
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, receiver, msg.as_string())
    smtp_server.quit()
    print('邮件发送成功，主题：%s' % mail_subject)


if __name__ == "__main__":
    content = '''
           你好，小明
       '''
    send_email("想你了", content)
