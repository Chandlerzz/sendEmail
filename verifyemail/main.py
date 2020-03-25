# main.py
# 03_create_data_sql.py
import sqlite3
# import verifyemail
import pandas as pd 
import os
import re

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

os.chdir("customer")
listAddress = [os.path.join(os.getcwd(),path) for path in os.listdir()]
listName = [re.split(r'\.',name)[0] for name in os.listdir()]
for i in range(len(os.listdir())):
    dataframe = pd.read_excel(listAddress[i])
    dataframe.insert(loc=0,column="validateValue",value=0)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS `%s` (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,email varchar(60),name varchar(60),istrue integer);"""%(listName[i]))
    for j in range(len(dataframe)):
        email=dataframe["电子邮件"][j]
        name = dataframe["联系人"][j]
        istrue= dataframe["validateValue"][j]
	    # list1=(email,name,istrue)
	    # list2=[list1]
        cursor.execute("INSERT INTO "+listName[i]+" (email,name,istrue) "+" VALUES (?,?,?)",(str(email), str(name), istrue))

    conn.commit()
    print(listName[i])

print('Dados inseridos com sucesso.')

conn.close()

# listIstrue = [0]*len(dataframe)
# 	try:
# 		istrue=verifyemail.verify_istrue(email)
# 		if istrue[email] ==True:
# 			listIstrue[i]=1
# 	except:
# 		print(email)

# dataframe["validateValue"]=istrue
# writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\1.xlsx")
# dataframe.to_excel(writer, sheet_name=sheet)
# writer.save()
