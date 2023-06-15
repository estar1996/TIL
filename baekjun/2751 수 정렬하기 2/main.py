import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for _ in range(N):
    l = int(input())
    lst.append(l)
lst.sort()
for i in lst:
    print(i)