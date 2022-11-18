import sys
sys.stdin=open('input.txt')
from collections import deque

def bfs(n,m):
    Q = deque()
    Q.append(n)
    while Q:
        now = Q.popleft()
        if now == m:
            return visited[now]
        if 1 <= now-1 <= 1000000 and not visited[now-1]:
            visited[now-1] = visited[now]+1
            Q.append(now -1)
        if 1<= now -10 <= 1000000 and not visited[now-10]:
            visited[now-10] = visited[now]+1
            Q.append(now-10)
        if now*2 <= 1000000 and not visited[now*2]:
            visited[now*2] = visited[now]+1
            Q.append(now*2)
        if now + 1 <= 1000000 and not visited[now+1]:
            visited[now+1] = visited[now]+1
            Q.append(now+1)


T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())

    visited = [0] * 1000001
    res = bfs(n,m)
    print("#{} {}".format(tc,res))