import sys
sys.stdin = open('input.txt')

dic = {0:5, 1: 3, 2:4,3:1, 4:2, 5:1 }
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))
for i in range(6):
    res = []
    temp = lst
    temp[0][i] = 0
    temp = lst[0][dic[i]]
    lst[0][dic[i]] = 0
    for j in range(1,N):