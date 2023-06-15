

n,m = map(int,input().split(':'))
def f(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i
x = f(n,m)

n /= x
m /= x
print(int(n),end=':')
print(int(m))
