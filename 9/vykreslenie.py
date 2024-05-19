import tkinter as tk


def nakresli_obrazok():
    color = ["black", "white"]
    y = 0
    for i in obrazok:
        x = 0
        line = i.split(' ')
        for j in line:
            for k in range(int(j)):
                canvas.create_rectangle(x, y, x, y, fill=color[0], outline=color[0])
                x += 1
            color = [color[1], color[0]]
        y += 1


def negative():
    canvas.delete('all')
    obrazok.seek(0)
    obrazok.readline()
    color = ["white", "black"]
    y = 0
    for i in obrazok:
        x = 0
        line = i.split(' ')
        for j in line:
            for k in range(int(j)):
                canvas.create_rectangle(x, y, x, y, fill=color[0], outline=color[0])
                x += 1
            color = [color[1], color[0]]
        y += 1


# cierna biela
obrazok = open("maturita/9/komprimovany_obrazok_1.txt", 'r', encoding="UTF-8")
dimensions = obrazok.readline().strip().split()
WIDTH, HEIGHT = int(dimensions[0]), int(dimensions[1])

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
button = tk.Button(root, text="negativ", command=negative)
button.pack()
nakresli_obrazok()

root.mainloop()