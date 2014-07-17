# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib

htmltext = urllib.urlopen("http://coop.khu.ac.kr/hall/menu1.php?sday=1405263600&cday=1405522800").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

for each in soup.findAll('td', attrs={'class': 'ft1'}):
	print each.text
