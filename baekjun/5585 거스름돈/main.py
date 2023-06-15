import sys
sys.stdin = open('input.txt')
N = int(input())

# 500, 100, 50, 10, 5, 1 엔

v = 1000 - N
res = 0
res += (v//500)
v -= (v // 500) * 500
res += (v // 100)
v -= (v//100) * 100
res += (v // 50)
v -= (v//50) * 50
res += (v // 10)
v -= (v//10) * 10
res += (v//5)
v -= (v//5) * 5
res += (v)
print(res)
