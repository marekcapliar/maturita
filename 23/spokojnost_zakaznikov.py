data = open("maturita/23/spokojnost_1.txt", 'r', encoding="UTF-8").readlines()
print("celkovy pocet vyjadreni je:", len(data))
hodiny = {}
for i in data:
    temp = i.strip().split()
    cas = int(temp[0][:2])
    temp_list = hodiny.get(cas, [])
    temp_list.append(temp[1])
    hodiny[cas] = temp_list
for i in hodiny:
    hodiny[i] = {"áno": hodiny[i].count("áno"), "nie": hodiny[i].count("nie")}

najspokojnejsia_hodina = max(hodiny, key=lambda x: hodiny[x]["áno"])
print("najspokojnejsia hodina je", najspokojnejsia_hodina, "s poctom ano", hodiny[najspokojnejsia_hodina]["áno"])
nespokojna_hodina = max(hodiny, key=lambda x: hodiny[x]["nie"])
print("nanejspokojnejsia hodina je", nespokojna_hodina, "s poctom nie", hodiny[nespokojna_hodina]["nie"])
relativna_spokojnost = {i: 0 for i in sorted(hodiny.keys())}
for i in hodiny:
    relativna_spokojnost[i] = int(hodiny[i]["áno"]/(hodiny[i]["áno"]+hodiny[i]["nie"])*100)
print("percenta spokojnosti:\n" + "\n".join([': '.join([str(i), str(relativna_spokojnost[i])+"%"]) for i in relativna_spokojnost]))
