import sys
sys.stdin = open('input.txt')

lst = []
tmp = 0

for _ in range(5):
    l = list(map(str,input()))
    lst.append(l)

for i in range(5):
    if len(lst[i]) > tmp:
        tmp = len(lst[i])


res = ['','','','','','','','','','','','','','','']
for i in range(5):
    for j in range(len(lst[i])):
        if j >= (len(lst[i])-1):
            break
        elif j >= 5:
            break
        else:
            res[i] += lst[j][i]


for i in range(5):
    print(res[i],end='')
#
