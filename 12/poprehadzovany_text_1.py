from random import shuffle

text = open("maturita/12/poprehadzovany_text1_vstup.txt", 'r', encoding="UTF-8").readlines()
poprehadzovany_subor = open("maturita/12/poprehadzovany_text1.txt", 'w', encoding="UTF-8")
print(''.join(text))
text = [i.strip().split() for i in text]
new_text = ""
for i in text:
    for word in i:
        inner_word = [j for j in word[1:-1]]
        shuffle(inner_word)
        shuffled_word = word[0] + ''.join(inner_word) + word[-1] if len(word) > 1 else word
        new_text += shuffled_word + ' '
    new_text += '\n'
print('\n'+new_text)
poprehadzovany_subor.write(new_text)
    