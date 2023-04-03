import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

arr = []
for _ in range(M):
    l = list(input())
    for i in range(N):
        if l[i] == 'B':
            l[i] = 1
        elif l[i] == 'R':
            l[i] = 2
        elif l[i] == "O":
            l[i] = 3
        elif l[i] == '.':
            l[i] = 0
        else:
            l[i] = 5
    arr.append(l)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def R(x,y):
    for i in range(1,N):
        if arr[x+i][y] == 0:
            arr[x+i][y] = arr[x][y]
            arr[x][y] = 0
        else:
            arr



print(arr)