import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

arr = []
for _ in range(M):
    l = list(map(int,input().split()))
    arr.append(l)

for i in range(N):
    for j in range(M):
        if arr[i][j] !='B'


def dfs(i,j):
