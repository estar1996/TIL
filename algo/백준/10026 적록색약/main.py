import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 1
        elif arr[i][j] == 'G':
            arr[i][j] = 2
        else:
            arr[i][j] = -1
visited = [[0]*N for _ in range(N)]



def red_dfs(x,y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k] % 4
        ny = y + dy[k] % 4

        if arr[nx][ny] == 1:
            if visited[nx][ny] != 1:
                red_dfs(nx,ny)

def green_dfs(x,y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k] % 4
        ny = y + dy[k] % 4

        if arr[nx][ny] == 1:
            if visited[nx][ny] != 1:
                red_dfs(nx,ny)





print(arr)