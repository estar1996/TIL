import sys
from collections import deque

sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N,M = map(int,input().split())
arr = []
Q = deque()
cnt = 0
for i in range(M):
    l = list(map(int,input().split()))
    arr.append(l)
    for j in range(N):  # 익은 토마토 큐에 저장
        if arr[i][j] == 1:
            Q.append([i, j])

def bfs():
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 0:
                Q.append([nx,ny])
                arr[nx][ny] = arr[x][y] + 1
bfs()
max_res = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            cnt = -1
        if arr[i][j] > max_res:
            max_res = arr[i][j]

if cnt != -1:
    print(max_res-1)
else:
    print(-1)
