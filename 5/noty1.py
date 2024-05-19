import tkinter as tk, math


def preformatuj(text):
    new_text = []
    line = []
    for i in text:
        line.append(i)
        if len(line) >= NOTES_IN_ONE_OSNOVA:
            new_text.append(line)
            line = []
    if len(line) != 0:
        new_text.append(line)
    return new_text


def create_osnova(y):
    for i in range(1, 6):
        canvas.create_line(0, y + NOTE_HEIGHT * i, WIDTH, y + NOTE_HEIGHT * i)


def insert_notes(y, notes):
    for x, note in enumerate(notes):
        canvas.create_oval((x + 1) * NOTE_WIDTH + x * NOTE_WIDTH//2, y + notes_as_number[note] * NOTE_HEIGHT//2, (x + 2) * NOTE_WIDTH + x * NOTE_WIDTH//2, y + notes_as_number[note] * NOTE_HEIGHT//2 + NOTE_HEIGHT)


text = open("maturita/5/noty.txt", 'r', encoding="UTF-8").read()
# c d e f g a h

root = tk.Tk()

NOTE_WIDTH = 20
NOTE_HEIGHT = 10
NOTES_IN_ONE_OSNOVA = 19
WIDTH = (NOTES_IN_ONE_OSNOVA + 1) * NOTE_WIDTH * 3 // 2
OSNOVA_HEIGHT = 7 * NOTE_HEIGHT
HEIGHT = 4 * OSNOVA_HEIGHT

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

text = preformatuj(text)
notes_descending = 'hagfedc'
notes_as_number = {notes_descending[i]: i for i in range(len(notes_descending))}
for i in range(len(text)):
    create_osnova(i * OSNOVA_HEIGHT)
    insert_notes(i * OSNOVA_HEIGHT + OSNOVA_HEIGHT//2 - NOTE_HEIGHT, text[i])

root.mainloop()