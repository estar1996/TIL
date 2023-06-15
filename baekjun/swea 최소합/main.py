import sys
sys.stdin = open("input.txt")

dx = [0,1]
dy = [1,0]

def dfs(x,y):
    global res,temp
    if res < temp:
        return
    if x == N-1 and y == N-1:
        res = temp
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            temp += lst[nx][ny]
            dfs(nx,ny)
            temp -= lst[nx][ny]
            visited.remove((nx,ny))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    res = 5000
    temp = lst[0][0]
    visited = []
    dfs(0,0)
    print("#{} {}".format(tc,res))