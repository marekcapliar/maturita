import random


def random_priklad():
    x1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    vysledok = x1*x2
    return [str(x1) + "*" + str(x2) + ' = ', vysledok]


priklady = []
for i in range(10):
    priklady.append(random_priklad())
print(priklady)
output = open("maturita/27/nasobilka_vystup.txt", 'w', encoding="UTF-8")
output.write('\n'.join([''.join([i[0], str(i[1])]) for i in priklady]))

i = 0
count = 0
body = 0
while len(priklady) != 0:
    count = count%len(priklady)
    vysledok = int(input(priklady[count][0]))
    if vysledok == priklady[count][1]:
        if i < 10:
            body += 1
        priklady.pop(count)
    else:
        count += 1
    i+=1
print("pocet bodov:", body)
