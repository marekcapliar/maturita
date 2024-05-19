hlasy = open("maturita/3/hlasovanie_1.txt", 'r', encoding="UTF-8")
vypadnuti = open("maturita/3/hlasovanie_vypadnuti.txt", 'r', encoding="UTF-8").readlines()

spocitane_hlasy = {str(i): 0 for i in range(5220, 5230)}
for i in hlasy:
    hlas = i.strip()
    spocitane_hlasy[hlas] += 1
print("pocet hlasov:", sum(spocitane_hlasy.values()))
print("hlasy podla sutaziacich:\n", '\n'.join([f"{i}: {spocitane_hlasy[i]}" for i in spocitane_hlasy]))
print("najmenej hlasov s vypadnutymi:", min(spocitane_hlasy, key=lambda x: spocitane_hlasy[x]))
for i in vypadnuti:
    spocitane_hlasy.pop(i.strip())
print("najmenej hlasov bez vypadnutych:", min(spocitane_hlasy, key=lambda x: spocitane_hlasy[x]))
