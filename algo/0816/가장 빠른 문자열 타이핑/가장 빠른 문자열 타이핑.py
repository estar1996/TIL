import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    
    cnt = 0 #중복 카운트
    for i in range(0,len(A)):
        if A[i:(i+len(B))] == B:
            
            
            cnt += 1
        print(i)
    # res = len(A) -(cnt*len(B)) + cnt # A의 길이는 A 타이핑 횟수
    # print("#{} {}".format(tc,res))





    