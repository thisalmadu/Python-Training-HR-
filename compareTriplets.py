import math
import os
import random
import re
import sys

# compare array and write the results ina text file
def compareTriplets(a, b):
    res = []
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice = alice+1
        else:
            if b[i] > a[i]:
                bob = bob+1
    res.append(alice)
    res.append(bob)
    return res

if __name__ == '__main__':
    fptr = open("compareTriplets.txt", 'w')

    a = map(int, raw_input().rstrip().split())
    b = map(int, raw_input().rstrip().split())
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
