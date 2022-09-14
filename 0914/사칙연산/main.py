import sys
sys.stdin = open("input.txt")


# 왼쪽 자식과 오른쪽 자식을 따로 저장하는 방법
# 값을 저장하는 배열도 하나 만든다
def post_order(v):                                      # 순회하고자 하는 노드의 번호 : v
    # 연산자에 따라서
    # 왼쪽자식 결과 - 오른쪽 자식 결과
    if value[v] not in '+-*/':
        return value[v]
    else:
        l_result = float(post_order(left[v]))
        r_result = float(post_order(right[v]))
        if value[v] == '*':
            return l_result * r_result
        elif value[v] == '+':
            return l_result + r_result
        elif value[v] == '/':
            return l_result / r_result
        else:
            return l_result - r_result


T = 10
for tc in range(1,T+1):
    N = int(input())
    left = [0] * (N+1)                                  # 왼쪽 자식을 저장할 배열
    right = [0] * (N+1)                                 # 오른쪽 자식을 저장할 배열
    value = [None] * (N+1)                              # 값 또는 연산자를 저장할 배열
    for i in range(N):
        data = input().split()
        if len(data) == 2:                              # 자식이 없는 경우, 단말 노드, 피연산자
            value[int(data[0])] = data[1]               # 인덱스 잘 확인해보기
        else:                                           # 자식이 있는 경우, 연산자
            value[int(data[0])] = data[1]
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
    # 후위 순회 하면서 계산하기
    result = post_order(1)
    print('#{} {}'.format(tc,int(result)))
