while n == 0:
    n = int(input())
    lst = [i for i in range(n+1,2*n)]
    for j in range(len(lst)):
        lst2 = [i for i in range(1,j)]
        for k in range(len(lst2)):
            if j % k