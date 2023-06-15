import sys
sys.stdin = open("input.txt")
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for a in range(1,N):
            if arr[i][j] == 1:
                if arr[i+a][j+a] != 2 and i+a < 5 and j+a < 5:
                    arr[i][j] += 1
                if arr[i+a][j-a] != 2 and i+a < 5 and j-a >= 0:
                    arr[i][j] += 1

                if arr[i-a][j+a] != 2 and i-a >= 0 and j+a < 5:
                    arr[i][j] += 1
                if arr[i-a][j-a] != 2 and i-a >= 0 and j-a >= 0:
                    arr[i][j] += 1
            if arr[i][j] == 5:
                arr[i][j] == 2

print(arr)

