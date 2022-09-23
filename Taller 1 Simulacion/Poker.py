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
    0.6245267489711934,
    0.41102880658436214,
    0.7802469135802469,
    0.9173662551440329,
    0.4520164609053498,
    0.12493827160493827,
    0.4546502057613169,
    0.40411522633744856,
    0.047407407407407405,
    0.23637860082304527,
    0.2673251028806584,
    0.5476543209876543,
    0.2625514403292181,
    0.041646090534979426,
    0.625679012345679,
    0.5331687242798354,
    0.7270781893004116,
    0.2814814814814815,
    0.04823045267489712,
    0.3236213991769547,
    0.5150617283950617,
    0.8077366255144033,
    0.831275720164609,
]

o = [
    0, #TD todos diferentes
    0, #1P Un par
    0, #2P Dos pares
    0, #T Tercia
    0, #TP Tercia y un par
    0, #P Poker (4 de un tipo)
    0, #Q quintilla
]
total = 0
p = [
    0.3024, #TD
    0.504, #1P
    0.108, #2P
    0.072, #T
    0.009, #TP
    0.0045, #P
    0.0001, #Q
    ]

E = []

x2s = []

def execute(numbers, decimals):
    x2Total = 0;    
    for number in numbers:
        dict = {}
        number = round(number, decimals)
        strNumber = str(number).split(".")[1]
        for i in range(decimals):
            try:
                digit = strNumber[i]
            except:
                digit = "0"

            try:
                dict[digit] += 1
            except:
                dict[digit] = 1
        dict2 = {1:0,2:0,3:0,4:0,5:0}
        for key in dict:
            dict2[dict[key]] += 1  

        global total
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
    for i in range(len(p)):
        prob = p[i]
        e = prob * total
        E.append(e)
        x2 = ((e-o[i])**2)/e
        x2s.append(x2)
        x2Total += x2
    print(o, total,"\n",p,"\n", E,"\n", x2s, "\nx2", x2Total)

execute(numbers, 5)

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
'''