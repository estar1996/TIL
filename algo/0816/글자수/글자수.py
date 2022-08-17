T = int(input())
 
for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
     
 
    res =[0] * len(str1)
    for i in range(len(str1)):
        for idx in range(len(str2)):
             
            if str1[i] == str2[idx]:
                res[i] += 1
             
    print('#{} {}'.format(tc,max(res)))
