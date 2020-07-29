import numpy
# Convert an int array to float array

def arrays(arr):
    na = numpy.array(arr,float)
    return na

arr = map(int,raw_input().strip().split(' '))
result = arrays(arr)
print(result)
