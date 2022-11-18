import sys
sys.stdin = open("input.txt")

M = int(input())
N = int(input())
if M == 2 or N == 2:
    res_lst = [[2]]
elif M == 1:
    M += 1
    res_lst = []
else:
    res_lst=[]
if M % 2 == 0:
    for i in range(M+1,N+1,2):
        if i != 1:
            res = [i]
        else:
            res = []
        for j in range(2,i):
            if i == 2:
                pass
            elif i % j == 0:
                res.append(10001)
                break
            elif i == 2:
                pass
            else:
                pass
        res_lst.append(res)
else:
    for i in range(M, N + 1, 2):
        if i != 1:
            res = [i]
        else:
            res = []

        for j in range(2, i):
            if i == 2:
                pass
            elif i % j == 0:
                res.append(10001)
                break
            elif i == 2:
                pass
            else:
                pass
        res_lst.append(res)



new_lst = []
for q in range(len(res_lst)):
    if len(res_lst[q]) == 1:
        new_lst.append(res_lst[q][0])

if len(new_lst) == 0:
    print(-1)
else:
    print(sum(new_lst))
    print(min(new_lst))