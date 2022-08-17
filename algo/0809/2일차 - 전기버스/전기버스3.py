import sys
sys.stdin = open('sample_input(2).txt')

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    M_num = list(map(int,input().split()))


    print(K,N,M)
    print(M_num)