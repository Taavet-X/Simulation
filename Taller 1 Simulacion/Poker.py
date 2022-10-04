import Values

def execute(numbers, decimals, nc):

    cats = [
    "TD todos diferentes",
    "1P Un par",
    "2P Dos pares o T para 3 decimales",
    "T Tercia",
    "TP Tercia y un par",
    "P Poker (4 de un tipo)",
    "Q quintilla",
    ]

    o = [
        0, #TD todos diferentes
        0, #1P Un par
        0, #2P Dos pares o T para 3 decimales
        0, #T Tercia
        0, #TP Tercia y un par
        0, #P Poker (4 de un tipo)
        0, #Q quintilla
    ]
    total = 0

    p5 = [
        0.3024, #TD
        0.504, #1P
        0.108, #2P
        0.072, #T
        0.009, #TP
        0.0045, #P
        0.0001, #Q
        ]

    p3 = [
        0.72, #TD
        0.27, #P
        0.01  #T
    ]

    E = [0,0,0,0,0,0,0]

    x2s = [0,0,0,0,0,0,0]

    x2Total = 0;    
    for number in numbers:
        dict = {}
        number = round(number, decimals)
        strNumber = str(number).split(".")[1]
        #Se recorren los digitos de la parte decimal y se cuentan
        #de manera que se tengan la cantidad de veces que cada digito aparece en el numero
        for i in range(decimals):
            #Se corrige el numero, ej 0.1 -> 1 -> 10000 para 5 decimales
            try:
                digit = strNumber[i]
            except:
                digit = "0"
            #incrementa si existe, define como 1 si no existe.
            try:
                dict[digit] += 1
            except:
                dict[digit] = 1
        #se cuentan los tipos de agrupaciones, cantidad de pares, tercias, entre otros.
        dict2 = {1:0,2:0,3:0,4:0,5:0}
        for key in dict:
            dict2[dict[key]] += 1  

        #global total
        if decimals == 5:
            p = p5
            if dict2[1] == 5:
                o[0] += 1 #TD
                total += 1
            elif dict2[1] == 3 and dict2[2] == 1:
                o[1] += 1 #P
                total += 1
            elif dict2[1] == 1 and dict2[2] == 2:
                o[2] += 1 #2P
                total += 1
            elif dict2[1] == 2 and dict2[3] == 1:
                o[3] += 1 #T
                total += 1
            elif dict2[2] == 1 and dict2[3] == 1:
                o[4] += 1 #TP
                total += 1
            elif dict2[1] == 1 and dict2[4] == 1:
                o[5] += 1 #P
                total += 1
            elif dict2[5] == 1:
                o[6] += 1
                total += 1
        elif decimals == 3:
            p = p3
            if dict2[1] == 3:
                o[0] += 1 #TD
                total += 1
            elif dict2[1] == 1 and dict2[2] == 1:
                o[1] += 1 #P
                total += 1
            elif dict2[3] == 1:
                o[2] += 1 #2P
                total += 1

    for i in range(len(p)):
        prob = p[i]
        e = prob * total
        E[i] = e
        x2 = ((e-o[i])**2)/e
        x2s[i] = x2
        x2Total += x2
    
    if decimals == 5:
        gl = 7 - 1
    else:
        gl = 3 - 2
    xcrit = Values.get(gl, nc) #Se obtiene el xcritico de la tabla de probabilidades
    strRes = "gl: " + str(gl) + "\nNivel de confianza: " + str(nc) + "\nX2calc: " + str(x2Total) + "\nX2crit: " + str(xcrit)
    if x2Total <= xcrit:
        strRes += "\nX2calc <= X2crit"
        strRes += "\n\nConclusión:\nEl resultado no permite rechazar la hipotesis de independencia"
    else:
        strRes += "\nX2calc > X2crit"
        strRes += "\n\nConclusión:\nSe rechaza la hipotesis de independencia"

    return cats, o, p, E, x2s, x2Total, strRes
    #print(o, total,"\n",p,"\n", E,"\n", x2s, "\nx2", x2Total)

'''
numbers = [
    0.29843621399176956,
0.8454320987654321,
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
]
print(execute(numbers, 3, 0.05))
'''
'''
12345	12345	5	TD
11234	1234		4	P
11223	123		3	2P
11123	123		3	T
11122	12		2	TP
11112	12		2	P
11111	1		1	Q

1 2 3 4 5
5			TD
3 1			P
1 2			2P
2 0 1 		T
0 1 1		TP
1 0 0 1		P
0 0 0 0 1     Q


Para 3 decimales

123
112
111

1 2 3
3
1 1
0 0 1
'''

