T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    tmp = max(lst)
    p_lst = []
    cnt1 = 0
    cnt2 = 0
    res = 0
    for i in range(N):
        lst[i] = tmp - lst[i]
        res += (lst[i] // 3) * 2
        p_lst.append(lst[i] % 3)
    for j in range(N):
        if p_lst[j] == 1:
            cnt1 += 1
        elif p_lst == 2:
            cnt2 += 1
    while 1:
        if cnt1 == 0:
            break
        elif cnt2 == 0:
            break
        cnt1 -= 1
        cnt2 -= 1
        res += 2

    if cnt1 > 0:
        res += (cnt1 * 2 - 1)
    if cnt2 > 0:
        res += (cnt2 * 2)

    print(f'#{tc} {res}')
