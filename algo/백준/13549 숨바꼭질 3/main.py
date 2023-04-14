import sys
from collections import deque
sys.stdin = open('input.txt')

N,K = map(int,input().split())
cnt = 0
visited = [False] * 100001
visited[N] = True
Q = deque(N)
def bfs(n):
    if n == K:
        return
    while Q:
        tmp = Q.popleft()
        next_position


//132321321