    n = int(input())
    arr = map(int, input().split())
    nar =[]
    mar = []
    k=0

    if (n>= 2 and n<=10) is True:
        for i in range(n):
            if (int(arr[i])>=-100 and int(arr[i])<=100) is True:
                nar.append(int(arr[i]))
                k = k+1
        m = max(nar)
        for i in range(k):
            if nar[i]!=m:
                mar.append(nar[i])

        print(max(mar))