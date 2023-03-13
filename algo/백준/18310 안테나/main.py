import sys
sys.stdin = open('input.txt')
N = int(input())
lst = list(map(int,input().split()))

lst = sorted(lst)
result = []
for k in range(2):
    tmp = len(lst) // 2 - 1 + k
    res = 0
    for i in range(len(lst)):
        if lst[i] - lst[tmp] > 0:
            res += (lst[i] - lst[tmp])
        else:
            res += (lst[tmp] - lst[i])
    result.append(res)

if result[0] <= result[1]:
    print(lst[len(lst)//2-1])
else:
    print(lst[len(lst)//2])