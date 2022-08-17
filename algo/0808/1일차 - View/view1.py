import sys
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    N = int(input())
    b_lst = list(map(int, input().split())) 

 
    res = 0
  
    for i in range(2, N-2):
       
        if b_lst[i] > b_lst[i-1] and b_lst[i] > b_lst[i-2] and b_lst[i] > b_lst[i+1] and b_lst[i] > b_lst[i+2]:
            a = b_lst[i] - b_lst[i - 2]
            b = b_lst[i] - b_lst[i - 1]
            c = b_lst[i] - b_lst[i + 1]
            d = b_lst[i] - b_lst[i + 2]
            min_abcd = a
            for a in [a, b, c, d]:
                if a < min_abcd:
                    min_abcd = a
            res += min_abcd
    
    print("#{} {}".format(tc, res))