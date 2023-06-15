import sys
sys.stdin = open("input.txt")

N = int(input())
N_lst = list(map(int,input().split()))

M = int(input())
M_lst = list(map(int,input().split()))


lst = list(set(N_lst) & set(M_lst))
res = []
for i in range(M):
    if M_lst[i] in lst:
        res.append(1)
    else:
        res.append(0)

print(*res)