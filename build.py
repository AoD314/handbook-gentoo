#!/usr/bin/python3 

from urllib.request import urlopen
import re, io

def create_chapter(link):
	#u = urlopen('http://www.calculate-linux.ru/main/ru/installing_calculate')
	#text = u.read().decode('utf-8')
	text = io.open('doc1.tmp', 'r').read().replace('<a href', '\n<a href')
	pattern = re.compile('<div class="wiki">.*</div>', re.S)
	r = re.findall(pattern, text)

	print ('LEN:' + str(len(r)))
	for s in r:
		pos = s.find('</div>')
		print(s[18:pos])


def main():
	#u = urlopen('http://www.calculate-linux.ru/main/ru/documentation')
	#text = u.read().decode('utf-8')
	f = io.open('doc.tmp', 'r')
	text = f.read().replace('<a href', '\n<a href')

	pattern = re.compile('<a href="/main/ru.*" class="wiki-page">.*</a>')
	r = re.findall(pattern, text)

	llink = []

	for s in r:
		b = 'wiki-page">'
		pb = s.find(b)
		pe = s.find('</a>')
		title = s[pb+len(b):pe]
		b = '<a href="'
		pb = s.find(b)
		pe = s.find('"', pb + len(b))
		link  = 'http://www.calculate-linux.ru' + s[pb+len(b):pe]
		llink = llink + [link]
		#print ( title + ': {' + link + '}')
	
	print ('total : ' + str(len(llink)))

	create_chapter('q')


if __name__ == "__main__":
	main()

