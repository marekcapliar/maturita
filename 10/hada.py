hry = open("maturita/10/hada.txt", 'r', encoding="UTF-8").readlines()
komprimovany_subor = open("maturita/10/komprimovany_hada.txt", 'w', encoding="UTF-8")

print("pocet hier:", len(hry))
print("najdlhsia hra:", len(max(hry, key=lambda x: len(x))) - 1)
for i in hry:
    current_letter = 'H'
    counter = 0
    for j in i:
        if j == current_letter:
            counter += 1
        else:
            napis = current_letter + ' ' + str(counter) + ' '
            komprimovany_subor.write(napis)
            current_letter = j
            counter = 1
    komprimovany_subor.write('\n')