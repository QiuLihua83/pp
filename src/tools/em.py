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
    
    msg = MIMEText('您好，附件是合同范本，敬请过目','text','utf-8')  #中文需参数‘utf-8'，单字节字符不需要
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