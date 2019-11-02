'''
XSSCon - 2019/2020
This project was created by menkrep1337 with 407Aex team. 
Copyright under the MIT license
'''
import requests, json
##### Warna ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
##### Styling ######
underline = "\033[4m"
##### Default ######
agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
line="—————————————————" 
#####################
def session(proxies,headers,cookie):
	r=requests.Session()
	r.proxies=proxies
	r.headers=headers
	r.cookies.update(json.loads(cookie))
	return r

logo=G+"""██████╗ ██╗    ██╗███╗   ██╗██╗  ██╗███████╗███████╗
██╔══██╗██║    ██║████╗  ██║╚██╗██╔╝██╔════╝██╔════╝
██████╔╝██║ █╗ ██║██╔██╗ ██║ ╚███╔╝ ███████╗███████╗ %s
██╔═══╝ ██║███╗██║██║╚██╗██║ ██╔██╗ ╚════██║╚════██║ %s
██║     ╚███╔███╔╝██║ ╚████║██╔╝ ██╗███████║███████║
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
<<<<<<< STARTING >>>>>>>
"""%(R+"{v0.5 Final}"+G,underline+C+"https://github.com/pwn0sec/PwnXSS"+N+G)
	
##=======
"""%(R+"{v0.5 Final}"+G,underline+C+"https://github.com/pwn0sec/PwnXSS"+N+G)
	
>>>>>>> branch 'master' of https://github.com/pwn0sec/PwnXSS
"""
