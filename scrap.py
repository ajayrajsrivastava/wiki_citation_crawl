#!/usr/bin/python
import requests
import re
import urllib
from bs4 import BeautifulSoup

print "Enter Wikipedia URL"
url=raw_input()
src=requests.get(url)
soup=BeautifulSoup(src.content,'lxml')

print "Enter 1.Citation"
print "Enter 2.Lines"
query=input()
if query==1:
    print "Get Lines for Citation:-"
    x=raw_input()
    pattern=re.compile('cite_note-*\w*-+'+x+'"')
    assert x>=1
    src1=(str)(soup.find_all('a'))
    src2=re.findall(pattern,src1)
    link=src2[0][:-1]
    for para in soup.find_all('p'):
        if link in p.sup.id:
            print para.text
elif query==2:
    print "Get Citation For lines:-"
    lines=raw_input()
    for para in soup.find_all('p'):
        if lines in para.text:
            print para.sup.text    
else:
    print "Wrong Query"

