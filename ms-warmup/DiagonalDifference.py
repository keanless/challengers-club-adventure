import math
import os
import random
import re
import sys

 

def diagonalDifference(arr):
    first = sum([arr[x][x] for x in range(len(arr))])
    sec = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(first - sec))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()