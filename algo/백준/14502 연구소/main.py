import sys
sys.stdin = open('input.txt')

N,M =map(int,input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

arr = []
for _ in range(N):
    l = list(map(int,input().split()))
    arr.append(l)

tmp = 2

for _ in range(50):
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 1 or arr[i][j] != 0:                # 바이러스를 만나면
                for x in range(4):
                    nx = i + dx[x]
                    ny = j + dy[x]
                    if M > nx >= 0 and N > ny >= 0:
                        if arr[nx][ny] == 0:
                            arr[nx][ny] = tmp + 1
                        elif arr[nx][ny] == 1:
                            pass
    tmp += 1



print(arr)