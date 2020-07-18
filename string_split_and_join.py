def split_and_join(line):
    s = line.split(" ")
    j = "-".join(s)
    return(j)

print('************************')
line = raw_input()
result = split_and_join(line)
print(result)
