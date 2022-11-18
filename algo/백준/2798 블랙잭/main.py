import sys
sys.stdin = open("input.txt")

N,M = map(int,input().split())
lst = list(map(int,input().split()))

sum_lst = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j != k:
                sum_lst.append(lst[i]+lst[j]+lst[k])


for a in range(len(sum_lst)):
    if sum_lst[a] > M:
        sum_lst[a] = 0

print(max(sum_lst))
