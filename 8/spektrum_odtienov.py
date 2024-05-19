import tkinter as tk


def spocitaj_odtiene(pixels):
    odtiene = {i: 0 for i in range(256)}
    for i in pixels:
        for j in range(0, len(i), 2):
            pixel = int(i[j]+i[j+1], 16)
            odtiene[pixel] += 1
    new_odtiene = {}
    for i in odtiene.keys():
        if odtiene[i] != 0:
            new_odtiene[i] = odtiene[i]
    return new_odtiene


def nakresli_histogram(odtiene):
    x = 0
    for i in odtiene:
        y = HEIGHT - int(odtiene[i]/najviac_odtienov*HEIGHT)
        canvas.create_rectangle(x, HEIGHT, x+1, y, fill="grey", outline='grey')
        x += 2


fr = open("maturita/8/ciernobiely_obrazok_1.txt", 'r', encoding="UTF-8")
dimensions = fr.readline().strip().split()
x, y = int(dimensions[0]), int(dimensions[1])
print(f"sirka: {x}\nvyska: {y}\npocet bodov: {x*y}")
pixels = fr.readlines()
pixels = [i.strip() for i in pixels]

root = tk.Tk()

odtiene = spocitaj_odtiene(pixels)
najviac_odtienov = max(odtiene.values())
print("pocet najcastejsieho odtiena:", najviac_odtienov)

WIDTH = len(odtiene)*2
HEIGHT = 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

nakresli_histogram(odtiene)

root.mainloop()