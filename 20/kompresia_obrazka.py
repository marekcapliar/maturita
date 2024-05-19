def spracuj_riadok(riadok):
    body = ['0', '1']
    i = 0
    count = 0
    new_riadok = ""
    while i < len(riadok):
        while riadok[i] == body[0]:
            count += 1
            i += 1
            if i == len(riadok):
                break
        new_riadok += str(count) + ' '
        count = 1
        i += 1
        body = [body[1], body[0]]
    return new_riadok[:-1]+'\n'


fr = open("maturita/20/kompresia_obrazka_1.txt", 'r', encoding="UTF-8")
dimensions = fr.readline().strip().split()
width, height = int(dimensions[0]), int(dimensions[1])
print(f"sirka: {width}, vyska: {height}, pocet bodov: {width*height}")
fw = open("maturita/20/kompresia_obrazka_vystup.txt", 'w', encoding="UTF-8")
fw.write(' '.join(dimensions) + '\n')

for i in fr:
    fw.write(spracuj_riadok(i))