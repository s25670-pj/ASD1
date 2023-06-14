import random

list = [random.randint(0, 1000000) for n in range(300000)]

with open('random.csv', 'w') as f:
    for number in list:
        f.write("%s\n" % number)

list.sort()
with open('sorted.csv', 'w') as f:
    for number in list:
        f.write("%s\n" % number)

list.sort(reverse=True)
with open('reversed.csv', 'w') as f:
    for number in list:
        f.write("%s\n" % number)
