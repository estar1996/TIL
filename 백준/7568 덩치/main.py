import sys
sys.stdin = open("input.txt")

N = int(input())

lst = []
for _ in range(N):
    WH = list(map(int,input().split()))
    lst.append(WH)

print(lst)

n_lst = [[0]*N]
for i in range(N):
    if lst[i][0]