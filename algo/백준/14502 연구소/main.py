import copy
from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs():
    graph = copy.deepcopy(arr)

    Q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                Q.append((i,j))
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                Q.append((nx,ny))
    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    result.append(cnt)

def makeWall(n):
    if n ==3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(n+1)
                arr[i][j] = 0

N,M =map(int,input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
for _ in range(N):
    l = list(map(int,input().split()))
    arr.append(l)
result = []
makeWall(0)
print(max(result))












