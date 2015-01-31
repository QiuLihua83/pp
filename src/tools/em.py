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

    sender = 'qiulihua83@163.com'
    receiver = 'qiulihua83@qq.com'
    subject = 'python email test'
    smtpserver = 'smtp.163.com'
    username = 'qiulihua83@163.com'
    password = 'qlhg_831105'
    
    msg = MIMEText('你好','text','utf-8')  #中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    print "in main. begin...."
    
    send_txt_email();
    
    print "in main.  end....."