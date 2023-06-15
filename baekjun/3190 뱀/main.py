N = int(input())        # 보드의 크기
K = int(input())        # 사과의 개수


arr = [[0] * N for _ in range(N)]

print(arr)
for _ in range(K):      # 사과의 위치
    x,y = map(int,input().split())
    arr[x][y] = 1

L = int(input())        # 뱀의 방향 변환 횟수
for _ in range(L):
    