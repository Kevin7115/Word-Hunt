from array import *
from merge_sort import mergesort
from solution import Solver


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


def getSolution(solver: Solver):
    arr = []
    print("Starting Solve")

    arr = solver.fullDfs()
    mergesort(arr)

    for i in range(len(arr)):
        print(arr[i], len(arr[i]))
    
    print(solver.getTime(), "seconds to search")
    solver.showBoard()

def play():
    solver = Solver()
    while True:
        letters = input("\nWhat are the letters: ")
        if letters == "quit":
            break
        if len(letters) == 16:
            solver.setBoard(arrayCreator(letters, 4))
            getSolution(solver)



if __name__ == "__main__":
    play()
    pass

# 7.129152059555054 seconds to search with old method
# 5.4060752391815186 seconds to search using same word twice
# 0.06101799011230469 seconds to search with trie method + refactoring