import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1,T+1):
    a, b = map(int,input().split())
    tmp = 0
    for i in range(2,b+1):
        a *= a
    res = a % 10

    print(res)