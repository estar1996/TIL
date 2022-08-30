import sys
sys.stdin = open("input.txt")




Nan = []
for _ in range(9):
    N = int(input())
    Nan.append(N)



result = []
for i in range(9):
    for j in range(i+1, 9):
        Nan_i = Nan[i]
        Nan_j = Nan[j]
        Nan[i] = 0
        Nan[j] = 0
        # print(i,j)
        if sum(Nan) == 100 :
            result = Nan
            break
        else:
            Nan[i] = Nan_i
            Nan[j] = Nan_j

print(*sorted(result)[2:], sep = "\n")

