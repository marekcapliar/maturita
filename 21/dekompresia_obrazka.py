def spracuj_riadok(riadok):
    body = ["0", '1']
    riadok = riadok.strip().split(' ')
    new_riadok = ""
    for i in riadok:
        new_riadok += int(i)*body[0]
        body = [body[1], body[0]]
    return new_riadok + '\n'


fr = open("maturita/21/dekompresia_obrazka_1.txt", 'r', encoding="UTF-8")
dimensions = fr.readline().strip().split()
width, height = int(dimensions[0]), int(dimensions[1])
print(f"sirka: {width}, vyska: {height}, pocet bodov: {width*height}")
fw = open("maturita/21/dekompresia_obrazka_vystup.txt", 'w', encoding="UTF-8")
fw.write(' '.join(dimensions) + '\n')

for i in fr:
    fw.write(spracuj_riadok(i))