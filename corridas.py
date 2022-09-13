def count(string):
    total = 0
    last = ""
    for char in string:
        if char != last:
            total += 1
            last = char
    print(string + " " + str(total))

count("sscsscscs")

def validarCrecimiento(list):
    res = ""
    lastValue = list[0]
    for value in list[1:]:
        if value > lastValue:            
            res += "+"
        elif value < lastValue:
            res += "-"
        lastValue = value
    print(res)

validarCrecimiento([1,2,3,4,5,3,2,1,5,6,1,7,8,9,3,1,4,6,5,8,3])
