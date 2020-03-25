# sendEmail.py
import yagmail
from content import content
from subject import subject
import sqlite3
from tools import tools
import time
import random
import schedule
import sys

num=int(sys.argv[1])
number = 0
emailValidate = tools
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
user = 'chandleroscar@foxmail.com'
password = 'hmkmrudnzfpabbhc'
# 发送邮箱
sender = 'chandleroscar@foxmail.com'

#链接邮箱服务器
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
users = cursor.execute("""SELECT * FROM cars WHERE id<?""",(1000*num,))
users = users.fetchall()
emails = [user[1] for user in users if user[3]==1]
conn.close()
yag = yagmail.SMTP( user=user, password=password, host=smtpserver)


def sendEmail(yag,emails,subject,content):
	global number 
	randnum = random.randint(1,len(subject))
	receiver = emails[number]
	try:
		yag.send(receiver,subject[randnum],content)
		print(number)
	except :
		print(receiver)
		print(number)
	number=number+1
	time.sleep(random.randint(1,200))
schedule.every(5).minutes.do(sendEmail,yag,emails,subject,content)


while True:
    schedule.run_pending()
 


			

       