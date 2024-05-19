data = open("maturita/11/bus_vytazenost.txt", 'r', encoding="UTF-8")
max_kapacita = int(data.readline())
zastavky = data.readlines()
zastavky = [i.strip().split(' ') for i in zastavky]
print("pocet zastavok:", len(zastavky))
print("nazvy zastavok:", ', '.join([' '.join(i[2:]) for i in zastavky]))
najviac_nad_ramec = 0
pocet_v_buse = 0
preplneny = []
for i in zastavky:
    pocet_v_buse += int(i[0]) - int(i[1])
    if pocet_v_buse > max_kapacita and najviac_nad_ramec < pocet_v_buse - max_kapacita:
        najviac_nad_ramec = pocet_v_buse - max_kapacita
        preplneny.append(' '.join(i[2:]))
print("preplneny bol na zastavke/kach:", ', '.join(preplneny))
print("najviac nad ramec:", najviac_nad_ramec)