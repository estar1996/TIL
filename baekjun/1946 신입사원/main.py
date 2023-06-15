import sys
input = sys.stdin.readline


T = int(input())
for _ in range(1,T+1):
    N = int(input())
    res = 0
    lst = [list(map(int,input().split())) for _ in range(N)]

    lst.sort()
    top = 0
    result = 1
    for i in range(1,N):
        if lst[i][1] < lst[top][1]:
            top = i
            result += 1

    print(result)