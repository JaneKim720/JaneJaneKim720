# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib

htmltext = urllib.urlopen("http://gall.dcinside.com/board/lists/?id=tree").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

for each in soup.findAll('td', attrs={'class': 't_subject'}):
	print each.a.text





