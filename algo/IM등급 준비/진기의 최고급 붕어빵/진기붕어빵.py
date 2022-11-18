import sys
sys.stdin = open("input (1).txt")

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())                  # N = 손님 수 M = 붕어빵을 만드는 시간 K = M시간에 걸쳐 만들 수 있는 붕어빵 수
    ar = list(map(int,input().split()))

    ar_num = len(ar)
    res = 0
    arr = sorted(ar)
    boong = [0]*(max(arr)+1)
    boong_num = 0
    for i in range(1,len(boong)+1):
        boong[i-1] = boong_num
        if i % M == 0:
            boong_num += K

    for j in arr:
        boong[j] -=1
    for k in range(len(boong)):
        if boong[k] < 0:
            res += 1
            break
        else:
            continue
    if res == 0:
        if boong[-1] > 0:
            res = 0
    print(res)