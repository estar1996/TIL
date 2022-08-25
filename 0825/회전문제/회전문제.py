import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    N_arr = list(map(int,input().split()))


    for _ in range(M):
        N_arr.append(N_arr.pop(0)) 
    

    print("#{} {}".format(tc,N_arr.pop(0)))