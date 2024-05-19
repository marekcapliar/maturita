import tkinter as tk


def open_text():
    text = open("maturita/15/zastavba_na_ulici.txt", 'r', encoding="UTF-8").readlines()
    new_text = []
    for i in text:
        line = i.strip().split()
        line[0], line[1] = int(line[0]), int(line[1])
        new_text.append(line)
    return new_text


def start():
    data = open_text()
    y = 170
    x = 20
    ids = []
    for i in data:
        if i[1] == 0:
            canvas.create_line(x, y, x+i[0], y, width=3, fill="green")
            x += i[0]
            # tu appendujem trava aby som ju preskakoval potom
            ids.append('trava')
            continue
        temp = canvas.create_rectangle(x, y, x+i[0], y-i[1], fill="grey")
        x += i[0]
        ids.append(temp)
    return ids


def on_button_press():
    text = entry.get()
    vykresli(int(text))


def vykresli(max_height):
    global ids, red_lines
    for i in red_lines:
        canvas.delete(i)
        red_lines.pop(0)
    for i in range(len(ids) - 1):
        if ids[i] != "trava" and ids[i+1] != "trava":
            my_building = canvas.coords(ids[i])
            next_building = canvas.coords(ids[i + 1])
            height_difference = abs(my_building[1] - my_building[3] - next_building[1] + next_building[3])
            if height_difference > max_height:
                red_lines.append(canvas.create_line(my_building[2], my_building[1], my_building[2], next_building[1], width=5, fill='red'))



root = tk.Tk()

WIDTH = 800
HEIGHT = 200
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="vykresli", command=on_button_press)
button.pack()
red_lines = []
ids = start()

root.mainloop()