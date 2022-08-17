import sys
sys.stdin = open('1.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    
    max_num = lst[0] #첫번째 숫자부터 비교하기 위해 lst[0]을 지정한다
    for i in lst:
        if i > max_num : # 만약 i번째 값이 max_num 보다 크다면 max_num의 값은 i번째 값이 된다.
            max_num = i
    min_num = lst[0]
    for a in lst:
        if a < min_num:
            min_num = a
    res = (max_num - min_num)

    print("#{} {}".format(tc,res))



    