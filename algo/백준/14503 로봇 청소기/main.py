import sys
from collections import deque
sys.stdin=open('input.txt')

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
cnt = 0
for _ in range(N):
    l = list(map(int, input().split()))
    arr.append(l)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c, d):
    global cnt
# commit
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
# ddddddddd
    for _ in range(4):
        d = (d - 1) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if arr[nx][ny] == 0:
            dfs(nx, ny, d)
            return
# com
    nx = r - dx[d]
    ny = c - dy[d]

    if arr[nx][ny] != 1:
        dfs(nx, ny, d)
    else:
        return

dfs(r, c, d)
# dd
print(cnt)
