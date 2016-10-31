#!/usr/bin/python
import re,urllib,traceback
from bs4 import BeautifulSoup
from sets import Set

def printLines(finalText):

    for elem in finalText:
        print elem

def setLink():
    
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            link['href'] = link['href']+'$'


def getLines(citation):
    
    setLink()
    
    refPattern = re.compile(r'#cite_note-*\w*-+'+citation+'\$')
    citPattern = re.compile('([^\.\]]+)(?:[\[\]\d+\.\"]+)?(?=\['+citation+'\])')

    finalText = Set()

    for a_tags in soup.find_all('a',href=refPattern):
        para = str(a_tags.parent.parent.text.encode('utf-8'))
        for text in re.findall(citPattern,para):
            finalText.add(text)
    printLines(finalText)
    

def printCitations(index,para):

    print para[index+1]
    if para[index+3] == '[':   #In case of Multiple Citations eg. [1][2][3]...
        printCitations(index+3,para)
            
def getCitation(lines):
    
    for p_tags in soup.find_all('p'):
        para = str(p_tags.text.encode('utf-8'))
        if lines in para:
            index = para.find(lines)+len(lines)
            printCitations(index,para)
                

print "Enter URL"
URL = raw_input()    

try:
    link = urllib.urlopen(URL)
except Exception:
    traceback.print_exc()


soup = BeautifulSoup(link,'html.parser')
print "1-Get Lines which have the given citation."
print "2-Get Citations of a particular lines."

query = input()
assert (query != 1 or query != 2),"Invalid Query"


if query == 1:
    print "Enter Citation"
    citation = raw_input()
    getLines(citation)
            

if query == 2:
    print "Enter Lines"
    lines = raw_input()
    getCitation(lines)    
