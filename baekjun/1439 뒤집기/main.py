import sys
# input = sys.stdin.readline()

s = list(input())
s1 = []
s2 = []
for i in range(len(s)):
    s1.append(int(s[i]))
    s2.append(int(s[i]))



res1 = 0
res2 = 0

for i in range(len(s)):
    if s1[i] == 0:
        s1[i] = 1
        for j in range(1,len(s)-i-1):
            if s1[i+j] == 0:
                s1[i + j] = 1
            else:
                break
        res1 += 1

for i in range(len(s)):
    if s2[i] == 1:
        s2[i] = 0
        for j in range(1, len(s) - i - 1):
            if s2[i + j] == 1:
                s2[i + j] = 0
            else:
                break
        res2 += 1
if res1 > res2:
    print(res2)
else:
    print(res1)