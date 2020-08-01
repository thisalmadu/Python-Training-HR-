import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum = sum + ar[i]
    return sum

if __name__ == '__main__':
    fptr = open("veryBigSum.txt", 'w')

    #ar_count = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
