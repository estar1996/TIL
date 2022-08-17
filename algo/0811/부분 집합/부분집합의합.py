import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())

    A = [0]*N
