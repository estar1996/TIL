# a = ['ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN'] 
import sys
sys.stdin = open('GNS_test_input.txt')




T = int(input())

for _ in range(1):
    tc = input()
    lst = list(input().split())
    res =[0]*10
    
    for i in lst:
        if i == 'ZRO':
            res[0] += 1
        elif i == 'ONE':
            res[1] += 1
        elif i == 'TWO':
            res[2] += 1
        elif i == 'THR':
            res[3] += 1
        elif i == 'FOR':
            res[4] += 1
        elif i == 'FIV':
            res[5] += 1
        elif i == 'SIX':
            res[6] += 1
        elif i == 'SVN':
            res[7] += 1
        elif i == 'EGT':
            res[8] += 1
        elif i == 'NIN':
            res[9] += 1

   

    # res3 = []
    # res3.append(res[0]*'ZRO ')
    # res3.append(res[1]*'ONE ')
    # res3.append(res[2]*'TWO ')
    # res3.append(res[3]*'THR ')
    # res3.append(res[4]*'FOR ')
    # res3.append(res[5]*'FIV ')
    # res3.append(res[6]*'SIX ')
    # res3.append(res[7]*'SVN ')
    # res3.append(res[8]*'EGT ')
    # res3.append(res[9]*'NIN ')

            
        
        # res[i] += 1
    res[0] = res[0]*'ONE'
    print(res)

