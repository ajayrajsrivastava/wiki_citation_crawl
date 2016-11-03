#!/usr/bin/python
import re,urllib,traceback
from bs4 import BeautifulSoup
from sets import Set

class WikiCrawl:
    ''' Crawling Wiki Data '''
                    
                        #Query-1
        
    def printLines(self,finalText):
        
        for elem in finalText:
            print elem
       
    def setLink(self):
        
        for self.link in self.soup.find_all('a'):
            if self.link.has_attr('href'):
                self.link['href'] = self.link['href']+'$' 
                
       
    def getLines(self,citation):
        
        self.setLink()
        refPattern = re.compile(r'#cite_note-*\w*-+'+citation+'\$')
        citPattern = re.compile('([^\.\]]+)(?:[\[\]\d+\.\"]+)?(?=\['+citation+'\])')

        finalText = Set() 
        for a_tags in self.soup.find_all('a',href=refPattern): 
            para = str(a_tags.parent.parent.text.encode('utf-8'))
            for text in re.findall(citPattern,para):
                finalText.add(text)
        self.printLines(finalText)
        
       
                        #Query-2
    
    def printCitations(self,startIndex,para):
    
        endIndex = para[startIndex:].find(']') #']'
        print para[startIndex+1:startIndex+endIndex] #[Digits] 
        nextCit = startIndex+endIndex+1 
        if nextCit<= len(para)-1 and para[nextCit] == '[':   #In case of Multiple Citations eg. [1][2][3]...
            self.printCitations(nextCit,para)
            
    def getCitation(self,lines):
    
        InPara = False
        for p_tags in self.soup.find_all('p'):
            #Search Para
            para = str(p_tags.text.encode('utf-8'))
            if lines in para:
                InPara = True
                startIndex = para.find(lines)+len(lines)+1 #'['
                self.printCitations(startIndex,para)
    
        if InPara != True:
            #Search Table
            for td_tags in self.soup.find_all('td'):
                tableText = str(td_tags.text.encode('utf-8'))
                if lines in tableText:
                    startIndex = tableText.find(lines)+len(lines) #'['
                    self.printCitations(startIndex,tableText)

    
    def getQuery(self):
        
        print "1-Get Lines which have the given citation."
        print "2-Get Citations of a particular lines."
        self.query = input()
        assert (self.query != 1 or self.query != 2),"Invalid Query" 
        
        
    
    def __init__(self,URL):
        
        self.URL = URL
        try:
            self.link = urllib.urlopen(URL) 
        except Exception:
            traceback.print_exc() 
        
        self.soup = BeautifulSoup(self.link,'html.parser') #html parsing
        self.getQuery() 
        
        

        if self.query == 1:
            print "Enter Citation"
            citation = raw_input()
            self.getLines(citation)
        
           
                                    
        if self.query == 2:
            print "Enter Lines"
            lines = raw_input()
            self.getCitation(lines)
            
            
#Test Object
obj = WikiCrawl("https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect")
