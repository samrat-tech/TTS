import re

class abbreviation(object):  
    def expand_abbreviations(self,text): 
        self.text=text
        file = open("n.txt", "r")
        lines = file.readlines()
        data = []
        for line in lines:
            a = line.strip()
            data.append(tuple(a.split("=")))

        # List of (regular expression, replacement) pairs for abbreviations:
        self._abbreviations = [(re.compile('\\b%s\\ ' % x[0], re.IGNORECASE), x[1]) for x in data]
        for regex, replacement in self._abbreviations:
            self.text= re.sub(regex, replacement + " ",self.text) 
        return self.text

    def lowercase(self):
        return self.text.lower()    

    def english_cleaners(self):
        """Pipeline for English text, including number and abbreviation expansion."""        
        return self.expand_abbreviations(self.lowercase())

    def __init__(self,text):
        self.text=text
        
        

 

# p1=abbreviation("I am LOL hello")
# print(p1.english_cleaners())

