fr = open("maturita/2/objednane_jedla.txt", 'r', encoding="UTF-8")

jedla = {"z": 0, "c": 0, "m": 0, "o": 0}
for i in fr:
    temp = i.strip().split(' ')[1]
    jedla[temp] += 1
print(sum(jedla.values()))

print("zelena:", jedla['z'])
print("cervena:", jedla["c"])
print("modra:", jedla["m"])
print("oranzova:", jedla['o'])

nedostatok = []
for i in jedla:
    if jedla[i] < 20:
        nedostatok.append(i)
if len(nedostatok) == 0 :
    print("kazde jedlo je dost")
else:
    print("nedostatky:", ', '.join(nedostatok))