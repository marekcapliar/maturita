from string import ascii_uppercase

veta = input("daj vetu: ")

tabulka = {ascii_uppercase[i]: (i%3+1)*f"{i//3+1}"+' ' for i in range(len(ascii_uppercase))}
tabulka[' '] = '0 '
sifrovana_veta = ""
for i in veta:
    if i in tabulka.keys():
        sifrovana_veta += tabulka[i]
    else:
        sifrovana_veta += i
print(sifrovana_veta[:-1])
pocty_cisel = {str(i): 0 for i in range(11)}
for i in pocty_cisel:
    pocty_cisel[i] = sifrovana_veta.count(i)
max_pocet = 0
max_policka = []
for i in pocty_cisel:
    if max_pocet == pocty_cisel[i]:
        max_policka.append(i)
    elif max_pocet < pocty_cisel[i]:
        max_policka = [i]
        max_pocet = pocty_cisel[i]
print("najviac vyskytujuce sa cisla:", ', '.join(max_policka))