# sendEmail.py
import yagmail
from content import content
from subject import subject
from chandler import chandler
import sqlite3
from tools import tools
import time
import random
import schedule
import sys


#邮件发送
def sendEmail(yag,emails,subject,content):
	localtime = time.localtime(time.time())
	hour = localtime[3]
	if hour>6 and hour<23:
		global number 
		randnum = random.randint(1,len(subject))
		receiver = emails[number][1]
		try:
			yag.send(receiver,subject[randnum],content)
			print("success:%s",receiver)
			print(emails[number][0])
		
		except :
			print("failer:%s",receiver)
			print(emails[number][0])
		number=number+1
		time.sleep(random.randint(1,200))

#测试邮件
def testEmail(sender):
	from chandler import chandler
	import yagmail
	yag = yagmail.SMTP(user=chandler[sender][0],password= chandler[sender][1],host=chandler[sender][2])
	yag.send('664837078@qq.com',"this is test","test")



if __name__ == "__main__":
	#表名
	tableName = sys.argv[1]
	#发件人ID
	idNumber = sys.argv[2]
	#发件人信息
	senderInfo = sys.argv[3]
	#sender 信息
	user = chandler[senderInfo][0]
	password = chandler[senderInfo][1]
	smtpserver = chandler[senderInfo][2]

	number = 0

	#连接数据库
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	#查询有用的email地址
	users = cursor.execute("SELECT * FROM "+tableName+" WHERE id> ?",(idNumber,))
	users = users.fetchall()
	emails = [[user[0],user[1]] for user in users if user[3]==1]
	conn.close()
	yag = yagmail.SMTP( user=user, password=password, host=smtpserver)
	schedule.every(5).minutes.do(sendEmail,yag,emails,subject,content)
	while True:
		schedule.run_pending()		

       