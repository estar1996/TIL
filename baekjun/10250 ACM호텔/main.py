import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    H,W,N = map(int,input().split())

    n = N//H +1
    n2 = N % H
    if N % H == 0:
        n = N//H
        n2 = H
    print(n2*100+n)