stu_lst = []
mark_lst = []
name_lst = []
nw_stu_lst = []
nw_mark_lst = []

for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    stu_lst.append([name,score])

for i in range(len(stu_lst)):
    mark_lst.append(stu_lst[i][1])

m = min(mark_lst)
for i in range(len(mark_lst)):
    if mark_lst[i] != m:
        nw_stu_lst.append(stu_lst[i])

for j in range(len(nw_stu_lst)):
    nw_mark_lst.append(nw_stu_lst[j][1])

for j in range(len(nw_stu_lst)):
    if nw_stu_lst[j][1]== min(nw_mark_lst):
        name_lst.append(nw_stu_lst[j][0])

name_lst.sort()

for j in range(len(name_lst)):
    print(name_lst[j])