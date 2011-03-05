#!/usr/bin/python3 

from urllib.request import urlopen
import re

def main():
	u = urlopen('http://www.calculate-linux.ru/main/ru/documentation')
	text = u.read().decode('utf-8')
	pattern = re.compile('<li><a href="/main/ru.*" class="wiki-page">.*</a></li>')
	p_name  = re.compile('>.*</a>')
	r = re.findall(pattern, text)

	print('found: ' + str(len(r)) + '\n')
	for s in r:
		pos = s.find('page">')
		print (s[pos+6:-9])
		


if __name__ == "__main__":
	main()

