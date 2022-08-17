import sys
sys.stdin = open("sample_input(3).txt")

T = int(input())
for tc in range(1,T+1):
    s = list(map(str,input()))
    lst = []
    
    for i in s:
        if lst and i == lst[-1]:        # 리스트의 top과 같다면 제거
            lst.pop()
        else:
            lst.append(i)
        
    print("#{} {}".format(tc,len(lst)))
