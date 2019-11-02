import requests
from lib.helper.Log import *
from lib.helper.helper import *
from lib.core import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing import Process

class crawler:
	
	visited=[]
	
	@classmethod
	def getLinks(self,base,proxy,headers,cookie):

		lst=[]
	
		conn=session(proxy,headers,cookie)
		text=conn.get(base).text
		isi=BeautifulSoup(text,"html.parser")
	
		
		for obj in isi.find_all("a",href=True):
			url=obj["href"]
			
			if url.startswith("http://") or url.startswith("https://"):
				continue
		
			elif url.startswith("mailto:") or url.startswith("javascript:"):
				continue
			
			elif urljoin(base,url) in self.visited:
				continue
				
			else:
				lst.append(urljoin(base,url))
				self.visited.append(urljoin(base,url))
			
		return lst

	@classmethod
	def crawl(self,base,depth,proxy,headers,level,method,cookie):

		urls=self.getLinks(base,proxy,headers,cookie)
		
		for url in urls:
			
			p=Process(target=core.main, args=(url,proxy,headers,level,cookie,method))
			p.start()
			p.join()
			if depth != 0:
				self.crawl(url,depth-1,base,proxy,level,method,cookie)
				
			else:
				break	