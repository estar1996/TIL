import sys
from collections import deque
sys.stdin = open('input.txt')

M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
Q = deque([])

for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                Q.append([h,n,m])


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while Q:
    x, y, z = Q.popleft()

    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]
        if 0 <= a < H and 0 <= b < N and 0 <= c < M and arr[a][b][c] == 0:
            Q.append([a, b, c])
            arr[a][b][c] = arr[x][y][z] + 1

res = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)

            res = max(res,max(arr[i][j]))


print(res-1)