import time

limit = 50000

list = []
dic = {}
for i in range(limit):
    list.append(i)
    dic[i] = 1

timeStart = time.time()
for i in range(limit):
    boolean = i in list
timeEnd = time.time()
print("List: ", timeEnd - timeStart)

timeStart = time.time()
for i in range(limit):
    try:
        value = dic[i]
    except:
        pass
timeEnd = time.time()
print("Dict: ", timeEnd - timeStart)