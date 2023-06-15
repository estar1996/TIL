import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for _ in range(N):
    l = list(map(int,input().split()))
    lst.append(l)
res_lst = sorted(lst,key = lambda x:(x[1],x[0]))


for i in range(len(res_lst)):
    print(*res_lst[i])