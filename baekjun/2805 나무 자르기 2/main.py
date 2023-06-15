N, M = map(int,input().split())
lst = list(map(int,input().split()))

mid = max(lst) // 2
temp = 0                # 전 기록
while 1 :
    tmp = 0

    for i in range(N):
        if lst[i] - mid >= 0:
            tmp += lst[i] - mid
    if tmp > M:
        if temp == -1:
            print(mid)
            break
        else:
            mid += 1
        temp == 1
    elif mid < M:
        if temp == -1:
            print(mid)
            break
        else:
            mid -= 1
        temp == 1
    else:
        print(mid)
        break
