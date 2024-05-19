from string import ascii_uppercase

text = open("maturita/13/tabulka_pocetnosti.txt", 'r', encoding="UTF-8").read()
print(text)
text = text.upper()
abeceda = {i: text.count(i) for i in ascii_uppercase}
print("pocet znakov", "\n".join([" - ".join([i, str(abeceda[i])]) for i in abeceda]))
bez_znakov = []
for i in abeceda:
    if abeceda[i] == 0:
        bez_znakov.append(i)
print("bez vyskytu v texte su pismena:", ', '.join(bez_znakov))
