from array import *
import json
import time

dict = 'words_dictionary.json'

class Dictionary:
    def __init__(self, file) -> None:
        self.dict = json.loads(open(file).read())

    def check(self, word):
        if word in self.dict:
            return True
        return False
    
    def checkPrefix(self, prefix):
        for word in self.dict:
            if word[:len(prefix)] == prefix:
                return True
        return False


class Solution: 
    def __init__(self, b: array) -> None:
        self.arr = b
        self.words = []
        self.realWords = []
        self.R = len(self.arr) - 1
        self.C = len(self.arr[0]) - 1
        self.library = Dictionary(dict)
        self.time = 0
          

    def showBoard(self) -> array:
        for i in range(self.R+1):
            print(self.arr[i]) 
    
    def getTime(self):
        return self.time

    def search(self, r, c, str = "", visited = []):
        
        if (r,c) not in visited: 
            visited += [(r, c)]

            if not (r > self.R or r < 0 or c > self.C or c < 0):

                str += self.arr[r][c]

                if len(str) < 10:

                    if len(str) > 4 and self.library.check(str) and str not in self.words:
                        self.words.append(str)
        
           
                    self.search(r, c+1, str, visited) #r 
                    self.search(r, c-1, str, visited) #l
                    self.search(r-1, c-1, str, visited) # u l 
                    self.search(r-1, c, str, visited) # u
                    self.search(r-1, c+1, str, visited) # u r
                    self.search(r+1, c-1, str, visited) # d l
                    self.search(r+1, c, str, visited) # d 
                    self.search(r+1, c+1, str, visited) # d r
        
            visited.remove((r,c)) 
        return self.words


    def fullSearch(self):
        startTime = time.time()
        for r in range(self.R + 1):
            for c in range(self.C + 1):
                self.realWords += self.search(r,c)
                print(r,c)
                self.words = []
        endTime = time.time()
        self.time = endTime - startTime
        return self.realWords
    
a = Dictionary(dict)
str = "ws"
print(a.checkPrefix(str))


#Backup: 
#self.search(r, c+1, str, visited) #r 
#self.search(r, c-1, str, visited) #l
#self.search(r-1, c-1, str, visited) # u l 
#self.search(r-1, c, str, visited) # u
#self.search(r-1, c+1, str, visited) # u r
#self.search(r+1, c-1, str, visited) # d l
#self.search(r+1, c, str, visited) # d 
#self.search(r+1, c+1, str, visited) # d r