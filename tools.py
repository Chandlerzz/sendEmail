# tools.py
import re

class tools:
	def __init__():
		pass
	def validateEmail(email):
		if re.match(r'^[a-zA-Z0-9-.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email)!=None:
			return 1
		else:
			return 0
