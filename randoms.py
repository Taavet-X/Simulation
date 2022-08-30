x0 = 27
a = 17
c = 0
m = 100

dic = {}

def x(n):
    if n == 0:
        return x0
    else:
        newX = (a * x(n-1)+c) % m
        print(newX)
        return newX

x(100)
