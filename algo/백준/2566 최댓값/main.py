import sys
sys.stdin = open('input.txt')


arr = []
for _ in range(9):
    l = list(map(int,input().split()))
    arr.append(l)

tmp = 0
x,y = 0,0
for i in range(9):
    for j in range(9):
        if arr[i][j] > tmp:
            tmp = arr[i][j]
            x,y = i,j
print(tmp)
print(x+1,y+1)
