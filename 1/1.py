fr = open("maturita/1/meteo_stanice.txt", 'r', encoding="UTF-8")
udaje = []
highest_temperature = -500
id_highest_temperature = ""
total_temp = 0
for i in fr:
    udaje.append(i.strip().split(' '))
    temperature = f"{udaje[-1][3][:3]}.{udaje[-1][3][-1]}"
    if temperature[0] == "+":
        temperature = float(temperature[1:])
    else:
        temperature = float(temperature)
    udaje[-1][3] = temperature
    if highest_temperature < temperature:
        highest_temperature = temperature
        id_highest_temperature = udaje[-1][0]
    total_temp += temperature
average_temp = total_temp/len(udaje)
print(f"pocet merani: {len(udaje)}")
print("namerane hodnoty:", '  '.join([str(i[3]) for i in udaje]))
print("najvyssia teplota:", highest_temperature, "\nstanica s najvyssou teplotou:", id_highest_temperature)
print("priemerna teplota:", average_temp)