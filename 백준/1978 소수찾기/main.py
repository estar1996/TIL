import sys
sys.stdin = open("input.txt")

N = int(input())
lst = list(map(int,input().split()))
res_lst = []
for i in range(len(lst)):
    res = [i]
    for j in range(lst[i]):

        if lst[i] == 1:
            res.append(101)
            pass
        if j < 2:
            pass
        elif lst[i] > 2:
            if lst[i] % j == 0:
                res.append(101)
                break
        else:
            pass
    res_lst.append(res)

cnt = 0
for k in range(len(res_lst)):
    if len(res_lst[k]) == 1:
       cnt += 1


print(cnt)