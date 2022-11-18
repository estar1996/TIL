
import sys
sys.stdin = open("sample_input(2).txt")


from collections import deque
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())                      # N = 화덕 크기  M = 피자 개수
    Ci = deque(enumerate(map(int,input().split())))
                         # Ci = 치즈 양
    N_lst = deque()
    for i in range(N):
        N_lst.append(Ci.popleft())

    # print(Ci)
    # print(N_lst)

    while len(N_lst) > 1 :
        N_p = N_lst.popleft()
        N_p = (N_p[0],N_p[1]//2)
        if N_p[1]  == 0:
            if Ci:
            # print(Ci)
                N_lst.append(Ci.popleft())
            else:
                pass
        else :
            N_lst.append((N_p))
        
    print("#{} {}".format(tc,N_lst[0][0]+1))
        
        
        


