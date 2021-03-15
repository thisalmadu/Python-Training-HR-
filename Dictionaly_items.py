# with user input
n = int(input())
student_marks = {}
if (n >= 2) and (n<=10) is True:
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float,scores)
        student_marks[name] = scores
    query_name = raw_input()
    #print(list(student_marks[query_name]))
    s_l = list(student_marks[query_name])
    avg = (s_l[0]+s_l[1]+s_l[2])/3
    print("{:.2f}".format(avg))
