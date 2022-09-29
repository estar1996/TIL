import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline

def bfs(graph,start,visited):
    global cnt
    Q = deque([start])
    visited[start] = True
    while Q:
        v = Q.popleft()
        res[v] = cnt
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                Q.append(i)
                visited[i] = True





N,M,R = map(int,input().split())
graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
res = [0] * (N+1)
cnt = 1
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for j in graph:
    j.sort()
bfs(graph,R,visited)

for i in range(1,len(res)):
    print(res[i])
