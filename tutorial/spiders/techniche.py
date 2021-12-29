# -*- coding: utf-8 -*-
import scrapy
import requests
import whoosh
import os, sys
from bs4 import BeautifulSoup,UnicodeDammit
# from whoosh.index import create_in
# from whoosh.fields import *
# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
# ix = create_in("indexdir", schema)
# writer = ix.writer()
urls = open('urlforTecniche.txt','w')
class Intranet(scrapy.Spider):
	name = "techniche"
	allowed_domains = ["http://techniche.org/"]
	start_urls = ["http://techniche.org/techniche15/"]

	def parse(self, response):
		hyper = response.xpath('//a/@href')
		# print('\n' + response.url + '\n')
		# source = requests.get(response.url) # --
		# #print('\n'+ source.text + '\n')
		#plain_text = source.text 				
		#print('\n' + plain_text + '\n')
		# curr_url = response.url             # --
		# #unicode(curr_url)
		# cur_url = curr_url.encode('utf-8','strict')  # --
		# soup = BeautifulSoup(source.text,'lxml') # --
		# soup.title.encode("utf-8")          # --
		# #print( "\n" + curr_url + "\n")
		# plain_text = soup.get_text()        # --
		# title_head = soup.title.string      # --
		#print( '\n' + plain_text + '\n')
		# writer.add_document(title=title_head, path=cur_url, content=plain_text)  # --
		# writer.commit()   # --
		for h in hyper:
			url = response.urljoin(h.extract())
			urls.write(url + '\n')
			yield scrapy.Request(url, callback=self.parse)
