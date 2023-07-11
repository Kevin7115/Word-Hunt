from array import *
from merge_sort import *
from solution import *


def arrayCreator(str: str, num) -> array:
    board = []
    arr = []
    for i in range(num):
        for j in range(num):
            start = j + (i*4)
            end = j+1 + (i*4)
            arr.append(str[start:end])
        board.append(arr)
        arr = []
    return board

def play(str):
    if len(str) == 16:
        print("Starting Solve")

        s1 = Solution(arrayCreator(str, 4))

        arr = s1.fullSearch()
        mergesort(arr)

        for i in range(len(arr)):
            print(arr[i], len(arr[i]))
        
        print(s1.getTime(), "seconds to search")
        s1.showBoard()


letters = "arsebthfieshylog"
play(letters)


