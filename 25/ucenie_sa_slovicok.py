slovicka = open("maturita/25/ucenie_sa_slovicok.txt", 'r', encoding="UTF-8").read()
slovicka = slovicka.split('\n')
pocet_slov = len(slovicka)
sjl_anj = input("zadaj jazyk sjl/anj: ")
uhadnute = []
neuhadnute = 0
i = 0 if sjl_anj == "sjl" else 1
while len(uhadnute) < pocet_slov//2:
    slovo = input(f"preloz {slovicka[i%len(slovicka)]}: ")
    if i%2 == 0:
        if slovicka[(i+1)%len(slovicka)] == slovo:
            uhadnute.append(slovo)
            temp = len(slovicka)
            slovicka.pop(i%temp)
            slovicka.pop((i)%temp)
        else:
            i +=2
            neuhadnute += 1
    else:
        if slovicka[(i-1)%len(slovicka)] == slovo:
            uhadnute.append(slovo)
            temp = len(slovicka)
            slovicka.pop(i%temp)
            slovicka.pop((i-1)%temp)
            print(slovicka)
        else:
            i +=2
            neuhadnute += 1
print("zle pokusy:", neuhadnute)
