import sys
sys.stdin = open("input.txt")
T = int(input())                                                #주사위 개수

arr = [list(map(int,input().split())) for _ in range(T)]


print(arr)


















# AF = []
# BD = []
# CE = []
# for i in range(T):
#     AF.append(arr[i][0])
#     AF.append(arr[i][5])
#     BD.append(arr[i][1])
#     BD.append(arr[i][3])
#     CE.append(arr[i][2])
#     CE.append(arr[i][4])





# print(AF)
# print(BD)
# print(CE)

























# A = []
# B = []
# C = []
# D = []
# E = []
# F = []
# AF = []
# BD = []
# CE = []
# for i in range(T):
#     A.append(arr[i][0])
#     B.append(arr[i][1])
#     C.append(arr[i][2])
#     D.append(arr[i][3])
#     E.append(arr[i][4])
#     F.append(arr[i][5])
#     AF.append(arr[i][0] + arr[i][5])
#     BD.append(arr[i][1] + arr[i][3])
#     CE.append(arr[i][2] + arr[i][4])

# print(max(sum(AF),sum(BD),sum(CE)))