import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    N = int(input())
    h_lst = list(map(int,input().split()))
    res=0
    
    for i in range(2,N-2):
        if h_lst[i] - h_lst[i-1] >= 2 and h_lst[i] - h_lst[i-2] >=2 and h_lst[i] - h_lst[i+1] >=2 and h_lst[i] - h_lst[i+2] >=2 :
            a = h_lst[i] - h_lst[i-2]
            b = h_lst[i] - h_lst[i-1]
            c = h_lst[i] - h_lst[i+1]
            d = h_lst[i] - h_lst[i+2]
            min_abcd = a
            for x in [a,b,c,d]:
                if x < a:
                    min_abcd = x
                res += 1

    print("#{} {}".format(tc,res))
        # m.append(max(temp[i-2],temp[i-1],temp[i+1],temp[i+2]))
        # for j in m:
        #     if temp[i] - m[j] > 2:
        #         res.append(temp[i-m])
        # if i+2 - m >= 2:
        #     res.append(i+2 - m)

