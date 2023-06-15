import math
N = list(input())
lst =[]
for i in range(len(N)):
    lst.append(int(N[i]))
lst.sort(reverse=True)
for j in lst:
    print(j,end='')