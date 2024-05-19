data = open("maturita/24/spokojnost_1.txt", 'r', encoding="UTF-8").readlines()
casy = [i.split()[0] for i in data]
prev_time = 0
dni = []
reakcie = 0
hodiny = {}
for i in range(len(casy)):
    time = int(casy[i][:2])*60 + int(casy[i][3:5])
    if prev_time > time:
        dni.append(reakcie)
        reakcie = 0
    reakcie += 1
    prev_time = time

    hodiny[int(casy[i][:2])] = hodiny.get(int(casy[i][:2]), 0) + 1

for i in sorted(hodiny):
    print(f"Hodina:{i} Reakcii zakaznikov:{hodiny[i]}")
print("pocet dni:", len(dni))
for i in range(1, len(dni)+1):
    print(f"{i}. den - pocet reakcii: {dni[i-1]}")