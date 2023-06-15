numbers = list(range(1, 10001))
lst = []
for num in numbers :
    for n in str(num):
        num += int(n)
    if num <= 10000:
        lst.append(num)

for l in set(lst) :
    numbers.remove(l)
for res in numbers :
    print(res)