## Basic Important Syntax

### Adjust a string output width

txt = "banana"

x = txt.rjust(10,"0")

print(x)

### Receive an input and convert directly to an integer array

arr = map(int,raw_input().strip().split(' '))

### Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")

f.write("File has the new content!")

f.close()

### Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")

f.write("Now the file has more content!")

f.close()

### open and read the file after the appending:

f = open("demofile3.txt", "r")

print(f.read())
