import sys
sys.stdin = open("input.txt")

for tc in range(1,5):
    s = list(map(int,input().split()))

    s1 = s[0:4]
    s2 = s[4::]
    
    temp1  = []
    temp2 = []
    if s2[0] < s1[0]:
        temp2 = s2
        temp1 = s1
        s2 = temp1
        s1 = temp2
    print(s2,s1)
    x1 = 0
    y1 = 1
    x2 = 2
    y2 = 3
    res = []

    if s1[x2] > s2[x1] and s1[y2] > s2[y1] :
        print("a")
    elif s1[x2] > s2[x1] and s1
   