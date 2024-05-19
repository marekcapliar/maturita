from string import ascii_lowercase, ascii_uppercase

text = input("daj oznam: ")
text = text.split(' ')
print("pocet slov:", len(text))
horedole = ["hore", "dole"]
new_text = ""
for i in text:
    if horedole[0] == "hore":
        new_text += i.upper()
    else:
        new_text += i.lower()
    horedole = [horedole[1], horedole[0]]
print(new_text)

dekompresia = ""
zaciatok_slova = 0
for i in range(1, len(new_text)):
    if new_text[i].isupper() != new_text[i-1].isupper():
        dekompresia += new_text[zaciatok_slova:i].lower() + ' '
        zaciatok_slova = i
dekompresia += new_text[zaciatok_slova::] + new_text[-1]
print(dekompresia[:-1])