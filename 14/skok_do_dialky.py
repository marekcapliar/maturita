data = open("maturita/14/skok_do_dialky.txt", 'r', encoding="UTF-8").readlines()
krajiny = {}
winner_score = 0
winner = []
for i in data:
    temp = i.strip().split()
    krajiny[temp[1]] = krajiny.get(temp[1], 0) + 1
    skoky = []
    for j in temp[2:]:
        skoky.append(int(j))
    najlepsi_vykon = max(skoky)
    if najlepsi_vykon == winner_score:
        winner.append(temp[0])
    elif najlepsi_vykon > winner_score:
        winner_score = najlepsi_vykon
        winner = [temp[0]]
print("zoznam krajin:", ', '.join(krajiny.keys()))
print("pocty sutaziacich z krajin:", '\n'.join([': '.join([i, str(krajiny[i])]) for i in krajiny]))
print("vitaz/i je/su:", ', '.join(winner))
