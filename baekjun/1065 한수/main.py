num = int(input())

cnt= 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))       # 문자열로 받아서 탐
    if i < 100:
        cnt += 1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        cnt += 1
print(cnt)