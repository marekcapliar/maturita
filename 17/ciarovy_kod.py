import tkinter as tk, random


def draw_barcode(x: int, y: int, barcode):
    H = 80
    W = 10
    canvas.create_rectangle(x + W, y, x+W-barcode[0], y+H, fill="black", outline="")
    for i in range(1, 7):
        canvas.create_rectangle(x + i*W +W, y, x+ i*W -barcode[i]+W, y+H-15, fill="black", outline="")
    canvas.create_rectangle(x + 8*W, y, x+8*W-barcode[-1], y+H, fill="black", outline="")
    canvas.create_text(x+W*1.1, y+H-15, text=barcode, font="Arial 7", anchor='nw')


def generate_barcode():
    code = [random.randrange(1, 10) for i in range(8)]
    print(code)
    draw_barcode(10, 10, code)


def iterate_barcodes(e):
    global barcodes
    canvas.delete("all")
    for i in range(4):
        if len(barcodes) == 0:
            return
        draw_barcode(10+100*(i%2), 10+100*(i//2), barcodes[0])
        barcodes.pop(0)
        print(barcodes)


def text_to_barcode():
    text = open("maturita/17/ciarovy_kod_1.txt", 'r', encoding="UTF-8").readlines()
    barcodes = []
    for i in text:
        line = i.strip()
        new_line = []
        for j in line:
            new_line.append(int(j))
        barcodes.append(new_line)
    return barcodes


root = tk.Tk()

WIDTH = 250
HEIGHT = 250
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

generate_barcode()
barcodes = text_to_barcode()
root.bind("<space>", iterate_barcodes)

root.mainloop()