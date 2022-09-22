#Cinco decimales
#mostrar la tabla chi cuadrado
#3 y de 5 decimales
def count(string):
    total = 0
    last = ""
    for char in string:
        if char != "*":
            if char != last:
                total += 1
                last = char
    print(string + " " + str(total))

def validarCrecimiento(list):
    res = "*"
    lastValue = list[0]
    for value in list[1:]:
        if value > lastValue:            
            res += "+"
        elif value < lastValue:
            res += "-"
        lastValue = value
    return res

data = [
    0.921, 0.804, 0.141, 0.601, 0.308, 0.163, 0.555,
    0.987, 0.392, 0.571, 0.536, 0.066, 0.860, 0.869,
    0.163, 0.511, 0.751, 0.441, 0.074, 0,437, 0.628,
    0.727, 0.282, 0.655, 0.606, 0.699, 0.590, 0.783,
    0.923, 0.511, 0.724, 0.489, 0.505, 0.395, 0.367,
    0.901, 0.718, 0.612, 0.863, 0.941, 0.998, 0.276
  ]


count(validarCrecimiento(data))