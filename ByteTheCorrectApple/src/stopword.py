#coding=utf8

import codecs
import os

def solve (file) :
	if not os.path.isfile (file) :
		print "file not exists "
		return 
	with codecs.open (file, 'r' , 'utf-8') as cin : 
		list = []
		while True :
			line = cin.readline ()
			if not line :
				break
			line = line.strip ()
			if len (line) > 0 :
				list.append(line)
		t = """"""
		for s in list :
			t += s + '_'
		print t
if __name__ == "__main__" :
	solve (file = './stopwords')
