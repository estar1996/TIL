import sys
sys.stdin = open('sample_input(2).txt')

T = int(input())
for tc in range(1,T+1):
    K, N, M= map(int, input().split()) 
    M_num = list(map(int, input().split()))

    res = 0
    for i in range(1,M):
        if M_num[i-3] - M_num[i-2] > K:
            res = 0
        elif M_num[0] > K:
            res = 0
        else:
            res =(N // K)
    print("#{} {}".format(tc,res))
    print(M_num[i])