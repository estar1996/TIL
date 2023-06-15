import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for i in range(N):
    age,name = map(str,input().split())
    lst.append([int(age),i,name])

lst = sorted(lst)

for j in range(N):
    print(lst[j][0],end=' ')
    print(lst[j][2])

