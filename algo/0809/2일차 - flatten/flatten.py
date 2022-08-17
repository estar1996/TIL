import sys
sys.stdin = open('input.txt')

def max_num():                          # 가장 큰 값의 인덱스를 구하는 함수
    max_value = -1
    max_idx = -1
    for i in range(len(lst)):
        if lst[i] > max_value : 
            max_value = lst[i]
            max_idx = i
    return max_idx
def min_num():                          # 가장 작은 값의 인덱스를 구하는 함수
    min_value = 300
    min_idx = -1
    for a in range(len(lst)):
        if lst[a] < min_value:
            min_value = lst[a]
            min_idx = a
    return min_idx

T = 10

for tc in range(1, T+1):
    N = int(input())            #덤프 가능 수
    lst = list(map(int, input().split()))

    for i in range(N):          #덤프 가능 수 만큼 반복
        lst[max_num()] -= 1     #lst 의 가장 큰 값에서 1을 빼고
        lst[min_num()] += 1     #lst 의 가장 작은 값에서 1을 더한다

    print("#{} {}".format(tc,lst[max_num()] - lst[min_num()]))
    # print(min_num(),max_num())