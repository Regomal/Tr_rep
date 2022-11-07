#Причесон
from random import randint

list_1 = [randint(0,50) for i in range(10)]
print(list_1)

dist = round(len(list_1) / 1.247)

for i in range(len(list_1)):
    for j in range(len(list_1) - dist):
        if list_1[j] > list_1[j+dist]:
            list_1[j], list_1[j+dist] = list_1[j+dist], list_1[j]
    dist -= 1
    if dist == 0:
        break

print(f"list_1 after sort: {list_1}")
