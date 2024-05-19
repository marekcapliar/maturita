import tkinter as tk


def zapis_obed(e):
    jedlo_id = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)[0] - 1
    jedla = ["z", "c", "m", "o"]
    objednavka = str(entry.get()) + ' ' + jedla[jedlo_id] + '\n'
    objednavky.write(objednavka)
    print(objednavka)


def setup():
    color = ["green", "red", "blue", "orange"]
    for i in range(4):
        canvas.create_rectangle(100*i, 100, 100*(i+1), 200, fill=color[i], tags="jedlo")
    canvas.create_text(WIDTH//2, 50, text="VYBER JEDLA", font="Arial 40 bold", fill="red")


objednavky = open("maturita/18/vyber_jedla.txt", 'w', encoding="UTF-8")

root = tk.Tk()

WIDTH = 400
HEIGHT = 230
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

label = tk.Label(root, text="kod studenta")
label.pack()
entry = tk.Entry(root)
entry.pack()
setup()
canvas.tag_bind("jedlo", "<Button-1>", zapis_obed)
root.mainloop()