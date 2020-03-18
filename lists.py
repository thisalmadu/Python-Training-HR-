if __name__ == '__main__':
    N = int(raw_input())

    cc = 0
    ar = []

    while cc < N:
        com = raw_input()
        sp = com.split()
        #print(sp[0])
        if sp[0]=="insert":
            ar.insert(int(sp[1]),int(sp[2]))
        elif sp[0]=="print":
            print(ar)
        elif sp[0]=="remove":
            ar.remove(int(sp[1]))
        elif sp[0]=="append":
            ar.append(int(sp[1]))
        elif sp[0]=="sort":
            ar.sort()
        elif sp[0]=="pop":
            ar.pop()
        elif sp[0]=="reverse":
            ar.reverse()

        cc = cc+1