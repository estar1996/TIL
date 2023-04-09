import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

visited = [[0] * M for _ in range(N)]
visited[r][c] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

def dfs(x, y, d):
    global cnt

    while True:
        if arr[x][y] == 0:
            cnt += 1
            arr[x][y] = 2

        found = False
        for i in range(4):
            nd = (d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]

            if arr[nx][ny] == 0:
                x, y, d = nx, ny, nd
                found = True
                break
            else:
                d = nd

        if not found:
            nd = (d + 2) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]

            if arr[nx][ny] == 1:
                break
            else:
                x, y = nx, ny

    return cnt

print(dfs(r, c, d))