import tkinter as tk


def preklop():
    for i in range(1, pocet_jednotiek + 1):
        x = (WIDTH//2 - canvas.coords(i)[0])*2
        canvas.move(i, x, 0)


def nakresli():
    for y in range(0, len(pixels)):
        for x in range(0, len(pixels[y]), 2):
            if pixels[y][x] == '1':
                canvas.create_rectangle(x//2*strana, y*strana, x//2*strana + strana, y*strana + strana, fill="black")


def kolko_jednotiek():
    counter = 0
    for i in pixels:
        for j in i:
            if j == '1':
                counter += 1
    return counter


root = tk.Tk()

fr = open("maturita/7/preklopenie_obrazka.txt", 'r', encoding="UTF-8")
WIDTH, HEIGHT = fr.readline().strip().split()
strana = 4
WIDTH, HEIGHT = int(WIDTH)*strana, int(HEIGHT)*strana
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

pixels = fr.readlines()
pixels = [i.strip() for i in pixels]
print("pocet pixelov:", WIDTH//strana*HEIGHT//strana)
pocet_jednotiek = kolko_jednotiek()
print("pocet jednotiek:", pocet_jednotiek)
button =tk.Button(root, text="preklop obrazok", command=preklop)
button.pack()

nakresli()

root.mainloop()