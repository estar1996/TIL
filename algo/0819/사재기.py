# import sys
# sys.stdin = open("input (1).txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    max_lst = lst[-1]
    for i in range(N):
        
