## Basic Important Syntax

### Adjust a string output width

txt = "banana"

x = txt.rjust(10,"0")

print(x)

### Receive an input and convert directly to an integer array

arr = map(int,raw_input().strip().split(' '))
