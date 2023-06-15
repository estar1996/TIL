import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

know_p = int(input())
if know_p > 0 :
    lst = list(map(int,input().split()))
else:
    lst = []



arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))




