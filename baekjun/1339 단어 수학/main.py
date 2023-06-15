import sys
sys.stdin = open("input.txt")

N = int(input())

lst = []

for _ in range(N):
    a = list(input())
    lst.append(a)

for i in range(len(lst[0])):
    for j in range(len(lst[1])):
        cnt = 0
        if lst[0][i] == lst[1][j]:
            cnt += 1
        


print(lst)