from array import *
import math


def merge(arr: array, left: array, right: array):
    l, r, a, = 0, 0, 0

    while l < len(left) and r < len(right):
        lstr = len(left[l])
        rstr = len(right[r])

        if lstr <= rstr:
            arr[a] = left[l]
            l += 1
        else: 
            arr[a] = right[r]
            r += 1
        a += 1
    
    while l < len(left):
        arr[a] = left[l]
        l += 1
        a += 1

    while r < len(right):
        arr[a] = right[r]
        r += 1
        a += 1

def mergesort(mixedArr: array):
    if len(mixedArr) == 1:
        return
    
    midpoint = math.floor(len(mixedArr)/2)

    leftArr = mixedArr[:midpoint]
    rightArr = mixedArr[midpoint:]

    mergesort(leftArr)
    mergesort(rightArr)

    merge(mixedArr, leftArr, rightArr)


