import sys
sys.stdin = open('input.txt')

T = int(input())
# 300 , 60, 10 초

A = (T // 300)
T -= A * 300
B = (T // 60)
T -= B * 60
C = (T // 10)
T -= C * 10

if T :
    print(-1)
else:
    print(A,B,C,end=' ')