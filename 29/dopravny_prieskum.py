fr = open("maturita/29/dopravny_prieskup.txt", 'r', encoding="UTF-8").readlines()
data = []
for i in fr:
    print(i)
    temp = i.strip().split(';')
    temp[0], temp[1] = int(temp[0]), int(temp[1])
    data.append(temp)
dlha = 200
standartna = 100
kratka = 50
max_cestujucich = 0
cestujuci = 0
automat = []
znamenie = []
for i in data:
    cestujuci += i[0] - i[1]
    max_cestujucich = max([max_cestujucich, cestujuci])
    if i[0] >= 10:
        automat.append(i[2])
    if i[0] < 3 or i[1] < 3:
        znamenie.append(i[2])
    print(i[2], "pocet cesujucich:", cestujuci)
if max_cestujucich <= kratka:
    print("kratka elektricka je gut")
elif max_cestujucich <= standartna:
    print("standartna elektricka je gut")
else:
    print("dlha elektricka je gut")
print("automaty daj na zastavku/y:", ', '.join(automat))
print("zastavky na znamenie:", ', '.join(znamenie))