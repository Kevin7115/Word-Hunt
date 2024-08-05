from array import *
from merge_sort import *
from solution import Solution


def arrayCreator(letters: str, num) -> array:
    board = []
    arr = []
    for i in range(num):
        for j in range(num):
            start = j + (i*4)
            end = j+1 + (i*4)
            arr.append(letters[start:end])
        board.append(arr)
        arr = []
    return board

def play(letters):
    if len(letters) == 16:
        print("Starting Solve")

        s1 = Solution(arrayCreator(letters, 4))

        arr = s1.fullSearch()
        mergesort(arr)

        for i in range(len(arr)):
            print(arr[i], len(arr[i]))
        
        print(s1.getTime(), "seconds to search")
        s1.showBoard()


letters = "deaghtinbrawploy"
play(letters)

# 7.129152059555054 seconds to search with old method
# 5.4060752391815186 seconds to search using same word twice