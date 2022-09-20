import math

generatedNumbers = {}

def execute(x0, a, m):
    x = x0
    for i in range(1000):
        Rn = x/m
        try:
            generatedNumbers[Rn]
            print("Periodo:", i)
            return
        except:
            generatedNumbers[Rn] = 1
        q = math.floor(m / a)
        r = m % a        
        x = a * (x % q) - r * math.floor(x / q)
        if x < 0:
            x += m
        #print("q",q,"r",r,"x",x)
        #return
    print("Periodo >=", m)

def save():
    file = open("GEM.txt", "w")
    for number in generatedNumbers.keys():
        file.write(str(number) + "\n")
    file.close()

#execute(x0 = 72, a=10, m=73)
execute(x0 = 123456789, a=7**5, m=2**31-1)
save()