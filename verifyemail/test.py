
import sqlite3
import verifyemail
import pandas as pd 
import os
import re
import schedule
import sys

num=sys.argv[1]


conn = sqlite3.connect(r'C:\Users\Administrator\Desktop\sendEmail\test.db')
cursor = conn.cursor()
def doCheck(cursor,verifyemail):
	global num
	user = cursor.execute("""SELECT * FROM electric WHERE id=?""",(num,))
	user=user.fetchone()
	email=user[1]
	try:
		istrue=verifyemail.verify_istrue(email)
		if istrue[email] == True:
			cursor.execute("""UPDATE electric set istrue=? WHERE id=?""",('1',num,))
			print("%s is true",email)
			conn.commit()
	except:		
		print("%s is false",email)
	num1=int(num)+1
	num=str(num1)
schedule.every(30).seconds.do(doCheck,cursor,verifyemail)

while True:
    schedule.run_pending()
conn.close()


