from string import ascii_lowercase


def sifruj(text):
    new_text = ""
    for i in range(len(text)):
        if text[i] in ascii_lowercase:
            num = ord(text[i]) - 97
            current_kluc = ord(kluc[i%len(kluc)]) - 96
            num = (num + current_kluc)%26 + 97
            new_text += chr(num)
        else:
            new_text += text[i]
    return new_text


def desifruj(text):
    new_text = ""
    for i in range(len(text)):
        if text[i] in ascii_lowercase:
            num = ord(text[i]) - 97
            current_kluc = ord(kluc[i%len(kluc)]) - 96
            num = (num - current_kluc)%26 + 97
            new_text += chr(num)
        else:
            new_text += text[i]
    return new_text


print("\n\n\n")
kluc = input("zadaj sifrovaci kluc: ")
text_subor = open("maturita/4/vstupny_text.txt", 'r', encoding="UTF-8")
text = text_subor.read()
sifrovany_text = open("maturita/4/zasifrovany_text_1.txt", 'r', encoding="UTF-8").read()
sifrovat = input("S/D: ")
if sifrovat == "S":
    print(sifruj(text))
else:
    print(desifruj(sifrovany_text))