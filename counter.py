dic = {}

data = [1,2,3,1,2,3,4,5,6,1,2,3]

for value in data:
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1

for key in dic:
    print(str(key) + " " + str(dic[key]))
