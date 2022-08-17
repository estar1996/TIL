import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    res = 0
    cnt = 0
    for i in range(len(A)-len(B)+1):
        if A[cnt:len(B)+cnt] == B:
            res += 1
            cnt = len(B) + cnt - 1
        cnt += 1
    res = len(A) - res*len(B) + res

    print("#{} {}".format(tc,res))