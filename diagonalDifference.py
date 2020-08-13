import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = 0
    for i in range(len(arr)):
        sum1 = sum1 + arr[i][i]
    sum2 = 0
    for j in range(len(arr)):
        sum2 = sum2 + arr[j][len(arr)-j-1]
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open("diagonalDifference.txt", 'w')

    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, raw_input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
