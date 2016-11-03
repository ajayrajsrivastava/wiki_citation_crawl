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
    

def printCitations(startIndex,para):
    
    endIndex = para[startIndex:].find(']')
    print para[startIndex+1:startIndex+endIndex] #[Any num of digits] 
    nextCit = startIndex+endIndex+1 
    if nextCit<= len(para)-1 and para[nextCit] == '[':   #In case of Multiple Citations eg. [1][2][3]...
        printCitations(nextCit,para)
            
def getCitation(lines):
    
    InPara = False
    for p_tags in soup.find_all('p'):
        #Search Para
        para = str(p_tags.text.encode('utf-8'))
        if lines in para:
            InPara = True
            startIndex = para.find(lines)+len(lines)+1 #'['
            printCitations(startIndex,para)
    
    if InPara != True:
        #Search Table
        for td_tags in soup.find_all('td'):
            tableText = str(td_tags.text.encode('utf-8'))
            if lines in tableText:
                startIndex = tableText.find(lines)+len(lines)+1 #'['
                printCitations(startIndex,tableText)

URL = raw_input()    

while True:
    try:
        link = urllib.urlopen(URL)
    except Exception:
        traceback.print_exc() #error stack trace


    soup = BeautifulSoup(link,'html.parser')
    
    query = input()
    assert (query != 1 or query != 2),"Invalid Query"

    
    if query == 1:
        citation = raw_input()
        getLines(citation)
            

    if query == 2:
        lines = raw_input()
        getCitation(lines)   
    
    print "\n"  
