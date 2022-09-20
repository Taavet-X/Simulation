generatedNumbers = {}

def execute(x0, a, c, m):
    x = x0
    for i in range(1000):
        Rn = x/m
        try:
            generatedNumbers[Rn]
            print("Periodo:", i)
            return
        except:
            generatedNumbers[Rn] = 1
        x = (x * a + c) % m
    print("Periodo >=", m)

def save():
    file = open("GLC.txt", "w")
    for number in generatedNumbers.keys():
        file.write(str(number) + "\n")
    file.close()

execute(x0 = 1, a=5, c=7, m=1024)
save()