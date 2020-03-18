n = int(input())
integer_list = map(int, input().split())
i = 0
tupar =[]

for i in range(0,n):
    tupar.append(integer_list[i])

print(hash(tuple(tupar)))