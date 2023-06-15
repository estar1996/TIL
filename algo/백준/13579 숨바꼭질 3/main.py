import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())

cnt = 0


def plus(x,c):
    c += 1
    x += 1
