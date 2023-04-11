import sys
from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과의 개수

arr = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 2

L = int(input())
lst1 = []
lst2 = []
for _ in range(L):
    s, d = map(str, input().split())
    s = int(s)
    lst1.append(s)
    lst2.append(d)

Q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dist = 0
cnt = 0


def bfs(x, y, dist):
    global cnt
    cnt += 1

    if x < 0 or x >= N or y < 0 or y >= N or (x, y) in Q:
        return

    Q.append((x, y))

    nx = x + dx[dist % 4]
    ny = y + dy[dist % 4]

    if arr[nx][ny] != 2:
        if (nx, ny) not in Q:
            if 0 <= nx < N and 0 <= ny < N:
                Q.append((nx, ny))
                Q.popleft()
                if cnt not in lst1:
                    bfs(nx, ny, dist)
                else:
                    for i in range(len(lst1)):
                        if lst1[i] == cnt:
                            if lst2[i] == 'D':
                                bfs(nx, ny, dist + 1)
                            else:
                                bfs(nx, ny, dist - 1)
    else:
        Q.append((nx, ny))
        arr[nx][ny] = 0
        if cnt not in lst1:
            bfs(nx, ny, dist)
        else:
            for i in range(len(lst1)):
                if lst1[i] == cnt:
                    if lst2[i] == 'D':
                        bfs(nx, ny, dist + 1)
                    else:
                        bfs(nx, ny, dist - 1)


bfs(0, 0, 0)
print(cnt - 1)
