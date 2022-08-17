import sys
sys.stdin = open('GNS_test_input.txt')


T = int(input())
A = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


for _ in range(1,T+1):
    tc,N = map(str,input().split())
    num_lst = list(map(str,input().split()))

    res = []

    for i in range(10):
        for x in num_lst:
            if A[i] == x:
                res.append(x)
    
    print(tc)
    print(*res)