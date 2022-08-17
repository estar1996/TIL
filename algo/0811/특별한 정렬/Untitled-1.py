from platform import java_ver
import sys
sys.stdin = open('sample_input(3).txt')



T = int(input())     # 테스트 케이스 개수
 
for t in range(1, T+1):
    N = int(input())  # 정수의 개수
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(1, 6):
        B.append(A[N-i])
        B.append(A[i-1])
    print(f'#{t} ', end='')
    for j in B:
        print(j, '', end='')
    print('')