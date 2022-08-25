import sys
sys.stdin = open("input (2).txt")

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(arr)
    cnt = 0
    for i in range(7):
        for j in range(7):
            for a in range(2):
                for b in range(2):
                    cnt += arr[i+a][j+b]
    for c in range(1,10):
        if