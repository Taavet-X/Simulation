import math


matrix = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
'''
matrix = [
    [18,30,20,21,25],
    [30,21,26,18,31],
    [22,19,22,32,25],
    [29,26,24,17,22],
    [25,26,21,27,23],
]
'''

def execute(numbers):
    for i in range(math.ceil(len(numbers)/2)):
        try:
            pair = (numbers[i*2], numbers[i*2 + 1])
            rowIndex = math.ceil(pair[0]/2*10)-1
            columnIndex = math.ceil(pair[1]/2*10)-1
            matrix[rowIndex][columnIndex] += 1
        except:
            print("The list lenght wasn't odd, the last number is not included")            
    print(*matrix, sep="\n")
    n = len(numbers)
    FE = (n/2) / 25
    X2calc = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            FO = matrix[i][j]
            matrix[i][j] = round((FE-FO)**2 /FE,2)
            X2calc += matrix[i][j]
    print("----------------------")
    print(*matrix, sep="\n")
    print(X2calc)


















list = [
    0.2,
    1.0,
    0.8269958847736626,
    0.8727572016460905,
    0.7234567901234568,
    0.8976131687242799,
    0.35818930041152264,
    0.17925925925925926,
    0.21267489711934157,
    0.7547325102880659,
    0.2128395061728395,
    0.7721810699588477,
    0.062386831275720166,
    0.8241975308641976,
    0.5761316872427984,
    0.2811522633744856,
    0.013333333333333334,
    0.6245267489711934,
    0.41102880658436214,
    0.7802469135802469,
    0.9173662551440329,
    0.4520164609053498,
]

#execute(list)