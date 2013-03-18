#!/usr/bin/python
#coding=utf-8
import smtplib
from email.MIMEText import MIMEText

mailSender = 'sender@126.com'
mailHost = "stmp.qq.com"
mailPort = 25

def sendEmail(mailUser, mailPass, toList , topic , htmlContent):
	'''
	toList : send to who
	topic  : the mail subject
	htmlContent : the mail content
	'''
	
	if htmlContent == '':
		print "htmlContent is null!!!"
		return False

	msg = MIMEText(htmlContent,"html","utf-8")
	msg["Subject"] = topic
	msg["From"] = sender
	msg["To"] = ";".join(toList.split(","))
	try:
		s = smtplib.SMTP()
		s.connect(mailHost,mailPort)
		s.login(mailUser,mailPass)
		s.sendmail(sender,toList.split(","),msg.as_string())
		s.close
		return True
	except Exception,e:
		print str(e)
		return False


if __name__ == "__main__":
	if not sendEmail('username', 'password', 'xxx@126.com', 'test' , '测试内容哦'):
		print "send email error!!!"
	else:
		print "send email success."
