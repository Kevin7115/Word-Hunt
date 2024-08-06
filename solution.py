from array import *
from trie import *
import time

class Solver: 
    def __init__(self):
        self.board = ""
        self.R, self.C = 0, 0

        self.words = set()
        self.full_list = set()
        
        self.library = Dictionary('words_dictionary.json')
        self.prefix_lib = PrefixTree().load("prefix_dictionary.json")

        self.time = 0
        self.max_word_len = 10

    def setBoard(self, b):
        self.board = b     
        self.R = len(self.board) - 1
        self.C = len(self.board[0]) - 1

    def showBoard(self):
        for i in range(self.R+1):
            print(self.board[i]) 
    
    def getTime(self):
        return self.time

    def dfs(self, start, word = "", visited = set()):
        def get_neighbors(coord):
            r,c = coord
            neighbors = [(r + x, c + y) 
                         for y in range(-1, 2) 
                         for x in range(-1, 2) 
                         if (r+x >= 0 and c+y >= 0) and (r+x <= self.R and c+y <= self.C) and not (x == 0 and y == 0)
                        ]
            return neighbors

        visited.add(start)
        if word in self.prefix_lib and len(word) < self.max_word_len:
            if word in self.library and not word in self.words:
                self.words.add(word)
            
            for neigh in get_neighbors(start):
                if neigh not in visited:
                    self.dfs(neigh, word + self.board[start[0]][start[1]], visited)
        visited.remove(start)
        return self.words
    
    def fullDfs(self):
        self.full_list = set()
        startTime = time.time()
        for r in range(self.R + 1):
            for c in range(self.C + 1):
                self.full_list = self.full_list | self.dfs((r,c))
                self.words = set()
        self.time = time.time() - startTime
        return list(self.full_list)
    
    
if __name__ == "__main__":
    pass
