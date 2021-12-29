# -*- coding: utf-8 -*-
import scrapy
import requests
import whoosh
#import os, sys
from bs4 import BeautifulSoup,UnicodeDammit
#from whoosh.index import create_in
#from whoosh.fields import *
#schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
#ix = create_in("indexdir", schema)
#writer = ix.writer()
urls = open('xvideos.txt','w')


class Intranet(scrapy.Spider):
	name = "xvideos"
	allowed_domains = ["xxx.com"]
	start_urls = ["http://www.xxx.com/"]

	def parse(self, response):
		hyper = response.xpath('//a/@href')
		#print('\n' + response.url + '\n')
		#source = requests.get(response.url) # --
		#print('\n'+ source.text + '\n')
		#plain_text = source.text 				
		#print('\n' + plain_text + '\n')
		#curr_url = response.url             # --
		#unicode(curr_url)
		#curr_url.encode('utf-8','ignore')  # --
		#soup = BeautifulSoup(source.text,'lxml') # --
		#soup.title.encode("utf-8")          # --
		#print( "\n" + curr_url + "\n")
		#plain_text = soup.get_text()        # --
		#title_head = soup.title.string      # --
		#print( '\n' + plain_text + '\n')
		#writer.add_document(title=title_head, path=curr_url, content=plain_text)
		#writer.commit()
		for h in hyper:
			url = response.urljoin(h.extract())
			str_url=str(url)
			# if url == "http://intranet.iitg.ernet.in/cclrs/" or url[:66] == "http://csea.iitg.ernet.in/csea/Public/web_new/index.php/activities" or url[:35]=="http://jatinga.iitg.ernet.in/~dppc/" or len(url) >101 or url == "http://jatinga.iitg.ernet.in/~csesoftwarerepo/":
			# 	continue
			# if "http://planningcommission.nic.in/" in str_url or "calendar" or "year" in str_url "mailto" in str_url or "javascript" in str_url or len(str_url) is 0:
			# 	continue
			if str(response.url) + '#' == str_url :
				continue
			urls.write(url + '\n')
			yield scrapy.Request(url, callback=self.parse)
