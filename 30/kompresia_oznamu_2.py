veta = input("daj oznam: ")
slova = veta.split(' ')
new_veta = ""
for i in slova:
    temp = i[0].upper() + i[1:].lower()
    new_veta += temp
print(f"oznam sa sklada z {len(slova)} slov")
print(new_veta)

new_slova = []
slovo = ""
for i in new_veta:
    if i.isupper():
        new_slova.append(slovo)
        slovo = ""
    slovo += i
new_slova.append(slovo)
print(' '.join(new_slova[1:]))
