import sys
sys.stdin=open('input.txt')
N = int(input())
M = int(input())
graph =[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
graph.sort()
visited =[0] * (N+1)
cnt = 1
res = []
for i in range(len(graph)):
    if len(graph[i]) > 0:
        if graph[i][0] == 1:
            for k in range(len(graph[i])):
                res.append(graph[i][k])

if len(set(res)) > 0:
    print(len(set(res))-1)
else:
    print(0)