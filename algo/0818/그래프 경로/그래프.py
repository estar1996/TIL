import sys
sys.stdin = open("sample_input(2).txt")

T =int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    start_end = []
    for _ in range(1,E+1):
        s_e = list(map(int,input().split()))
        start_end.append(s_e)
    # print(start_end)
    S, G = map(int,input().split())
    

    lst = []  ##사용한 간선을 담는 리스트

    
    for _ in range(len(start_end)+1):
       
        res = 0
        for i in start_end:   #start_end  2중배열 돌리는  for문
            if i in lst:
                pass
            elif i[1] == G:
                lst.append(i)
        for i in start_end:    
            if res ==1:
                break
            for a in lst:
                if a[0] == i[1]:  ###도착지
                    lst.append(i)
                if lst[-1][0] == S:
                    res =1

                    break 
        if lst and lst[-1][0] == S:
            res = 1
            break
    

    print("#{} {}".format(tc,res))
    print(S,G)
    print(lst)
    # print(S, G)


    