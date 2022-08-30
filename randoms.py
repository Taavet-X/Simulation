x0 = 5
a = 5
c = 13
m = 7

def x(n):
    if n == 0:
        return x0
    else:
        newX = (a * x(n-1)+c) % m
        print(newX)
        return newX

x(10)
