import sys
sys.stdin = open('input.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N,M = map(int,input().split())

arr = []
for _ in range(N):
    l = list(map(int,input()))
    arr.append(l)
cnt = 0
def dfs(x,y):
    global cnt
    cnt += 1
    for i in range(N):
        for j in range(M):


    return 0

print(arr)
