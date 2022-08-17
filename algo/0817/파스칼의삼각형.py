import sys
sys.stdin = open("input (1).txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    res = []

    for i in range(N):
        lst = []
        for j in range(i+1):
            if j == 0 or j == i:
                lst.append(1)
            else:
                lst.append(res[i-1][j-1]+res[i-1][j])
        res.append(lst)

    print("#{}".format(tc))
    for a in res:
        print(*a)