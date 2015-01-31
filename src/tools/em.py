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
    
    sender = 'qiulihua83@163.com'
    pwd = 'qlhg_831105'
    receivers = 'qiulihua83@qq.com'   #['qiulihua83@qq.com', 'qiulihua83@sohu.com']
    subject = '您好，这是合同范本，敬请过目'
    filepath = '/Users/qiulihua/Downloads/meiwei-qizi.torrent'
    filename = 'meiwei-qizi.torrent'
    
    SLEEP_SECS = 5
    MAX_TIMES = 20
    index = 0
    while(index < MAX_TIMES):
        send_attach_email(sender=sender, pwd=pwd, receivers=receivers, subject=subject,filepath=filepath, filename=filename);
        print "the email %d  sent...\n" % (index)
        sleep(SLEEP_SECS)
        index = index + 1
    
    print "in main.  end....."
    
    