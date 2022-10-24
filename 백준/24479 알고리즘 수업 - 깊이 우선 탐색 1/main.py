import sys
sys.stdin = open('input.txt')
N,M,R = map(int,input().split())

def dfs(arr,R,visited):
    global cnt
    visited[R] = cnt
    arr[R].sort(reverse=True)
    for i in arr[R]:
        if visited[i] ==0:
            cnt += 1
            dfs(arr,i,visited)

visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
cnt = 1
print(arr)
# dfs(arr,R,visited)
# for i in range(1,N+1):
#     print(visited[i])