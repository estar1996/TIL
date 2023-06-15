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

<<<<<<< Updated upstream
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c, d):
=======
dx = [0,1,0,-1]
dy = [1,0,-1,0]
res = []
def dfs(r,c,d):
>>>>>>> Stashed changes
    global cnt
# commit
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
<<<<<<< Updated upstream
# ddddddddd
    for _ in range(4):
        d = (d - 1) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if arr[nx][ny] == 0:
            dfs(nx, ny, d)
=======
        res.append((r,c))
        for i in range(4):
            nx = dx[(d+i) % 4]
            ny = dy[(d+i) % 4]
            if arr[r+nx][c+ny] == 0:
                dfs(r+nx,c+ny,(d+i-1) % 4)

        nx = dx[d-1]
        ny = dy[d-1]
        if r-nx > 0 and c-ny >0 and r-nx < N and c-ny <M:
            if arr[r-nx][c-ny] == 0:
                dfs(r-nx,c-ny,d-1)
    else:
        nx = dx[(d+2) % 4]
        ny = dx[(d+2) % 4]
        if nx > 0 and ny > 0 and nx < N and ny < M:

            dfs(nx,ny,d)
        else:
>>>>>>> Stashed changes
            return
# com
    nx = r - dx[d]
    ny = c - dy[d]

    if arr[nx][ny] != 1:
        dfs(nx, ny, d)
    else:
        return

<<<<<<< Updated upstream
dfs(r, c, d)
# dd
=======
dfs(r,c,d)

print(res)

>>>>>>> Stashed changes
print(cnt)
