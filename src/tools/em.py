#coding:utf-8

import email;
import mimetypes
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText  
from email.MIMEImage import MIMEImage
from email.header import Header
import smtplib
from time import sleep

#===================================================================================================
# import smtplib,email,sys  
# from email.Message import Message
#===================================================================================================



def send_attach_email(sender, pwd, receivers, subject, filepath, filename):
    #邮件发送者
    smtpserver = 'smtp.163.com'
    username = sender
    password = pwd
    
    print "sender=%s, username=%s, password=%s, receivers=%s" %(sender, username, password, receivers)
    #组合邮件
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject 
    
    txt = MIMEText('您好，附件是合同范本，敬请过目','text','utf-8')  #中文需参数‘utf-8'，单字节字符不需要
    msg.attach(txt)
    
    #构造附件
    att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="' + filename + '"'
    msg.attach(att)
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    print "in main. begin...."
    
    sender = 'sleepwithu@163.com'
    pwd = '056239'
    receivers =  'lix@dayxar.com'   #'qiulihua83@qq.com'
    subject = '我和王总把草稿打好了，麻烦看一下是否合适，谢谢'
    filepath = '/Users/qiulihua/Desktop/31.zip'
    filename = '31.zip'
    
    SLEEP_SECS = 1800
    MAX_TIMES = 100
    index = 0
    while(index < MAX_TIMES):
        send_attach_email(sender=sender, pwd=pwd, receivers=receivers, subject=subject,filepath=filepath, filename=filename);
        print "the email %d  sent...\n" % (index)
        sleep(SLEEP_SECS)
        index = index + 1
    
    print "in main.  end....."
    
    