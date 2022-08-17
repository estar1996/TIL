T = int(input())

for tc in range(1,T+1):
    string = list(map(str,input()))
    open_n = 0
    open_m = 0
    close_n = 0
    close_m = 0
    res = 0
    for i in string:
        if i == '(' :
            open_n += 1
        elif i == '{':
            open_m += 1
        elif i == '}':
            close_m += 1
        elif i == ')':
            close_n += 1
        else:
            pass
    if open_n == close_n and open_m == close_m:
        res = 1
    else:
        res = 0
    print("#{} {}".format(tc,res))