import random

slovo = random.choice(open("maturita/26/obesenec.txt", 'r', encoding="UTF-8").readlines()).strip()
# slovo je v liste nech hladam cez index
hada_slovo = ['.' for i in range(len(slovo))]
vyhra = False
for i in range(10):
    print(''.join(hada_slovo), "pokus cislo", i+1)
    pismeno = input("hadaj pismenko: ")
    if pismeno in slovo:
        id_pismeno = []
        for i in range(len(slovo)):
            if slovo[i] == pismeno:
                id_pismeno.append(i)
        for i in id_pismeno:
            hada_slovo[i] = pismeno
    if ''.join(hada_slovo) == slovo:
        vyhra = True
        break
print("VYHRAL" if vyhra else "PREHRAL")