text = open("maturita/16/sutaz_vbehu.txt", 'r', encoding="UTF-8").readlines()
data = {}
for i in text:
    temp = i.strip().split()
    data[temp[0]] = int(temp[1])
print("pocet zucastnenych sportovcov:", len(data))
print('\n'.join([f"Sutaziaci {i} dobehol do ciela za {data[i]} sekund" for i in data]))
winner = min(data, key=lambda x: data[x])
print(f"najlepsi sutaziaci je {winner} s casom {data[winner]//60} min. {data[winner]%60} sek.")