from collections import deque


def dfs(x,y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        return True
    return False

graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
n = 5
m = 5

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)