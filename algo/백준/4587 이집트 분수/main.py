import sys
sys.stdin = open('input.txt')

M,N = map(int,input().split())
s,m = 3,4

res = []
for _ in range(2):

    if m % ((m//s)) == 0:
        s -= (m//((m//s)))
        print((m//s))
    else:

        s *= (m//s+1)
        s -= m
        m *= (m//s + 1)
        print(m)

