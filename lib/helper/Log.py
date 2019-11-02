'''
PwnXSS - 2019/2020
This project was created by Andripwn with Pwn0sec team. 
Copyright under the MIT license
'''
from lib.helper.helper import * 
from datetime import datetime
class Log:

	@classmethod
	def info(self,text):
 		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+G+"INFO"+N+"] "+text)
 
	@classmethod
	def warning(self,text):
		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+Y+"WARNING"+N+"] "+text)

	@classmethod
	def high(self,text):
 		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+R+"CRITICAL"+N+"] "+text)
 		