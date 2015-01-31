#coding:utf-8

import email;
import mimetypes
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText  
from email.MIMEImage import MIMEImage
from email.header import Header
import smtplib

#===================================================================================================
# import smtplib,email,sys  
# from email.Message import Message
#===================================================================================================



def send_txt_email():
    #邮件发送者
    sender = 'qiulihua83@163.com'
    smtpserver = 'smtp.163.com'
    username = 'qiulihua83@163.com'
    password = 'qlhg_831105'
    #邮件接收者
    receiver = 'qiulihua83@qq.com'
    #邮件标题
    subject = '您好，这是合同范本，敬请过目'
    
    #组合邮件
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject 
    
    txt = MIMEText('您好，附件是合同范本，敬请过目','text','utf-8')  #中文需参数‘utf-8'，单字节字符不需要
    msg.attach(txt)
    
    #构造附件
    att = MIMEText(open('/Users/qiulihua/Documents/pics/d043ad4bd11373f0fa6229a1a70f4bfbfbed04aa.jpg', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="d043ad4bd11373f0fa6229a1a70f4bfbfbed04aa.jpg"'
    msg.attach(att)
    
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    print "in main. begin...."
    
    send_txt_email();
    
    print "in main.  end....."