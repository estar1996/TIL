input1 = [900 ,901 ,902 ,903 ,904 ,905 ,906 ,907 ,908 ,909 ,910 ,911 ,912 ,913 ,914 ,915 ,916 ,917 ,918 ,919]

lst = []
for i in range(len(input1)):
    lst.append(input1[i])
    cnt = -1
    if len(lst) > 1:
        for j in range(len(lst)-1):
            if lst[len(lst) -1 -j] > lst[len(lst) -j]:
                lst[len(lst) - 1 - j], lst[len(lst) - j] = lst[len(lst) - j], lst[len(lst) - 1 - j]


print(lst)