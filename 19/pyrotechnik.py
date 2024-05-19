import tkinter as tk, random


def timer():
    global time, end
    if end:
        return
    time -= 1
    canvas.itemconfig(clock, text=time)
    if time <= 0:
        canvas.delete('all')
        end = True
        return
    canvas.after(1000, timer)


def setup():
    colors = ["green", 'red', 'grey', 'blue', 'orange']
    canvas.create_text(WIDTH//2, 50, text="Pyrotechnik", anchor='center', fill="blue", font="Arial 30 bold")
    canvas.create_text(WIDTH//2, 80, text="oznac spravny kablik", font="Arial 10 bold")
    cables = []
    for i in range(len(colors)):
        cables.append(canvas.create_rectangle(50, 100 + 10*i, 300, 100 + 10*(i+1), fill=colors[i], tags="cable"))
    correct_cable = random.choice(cables)
    clock = canvas.create_text(320, 100, text=time, fill="red", anchor='nw', font="Arial 30 bold")
    print(correct_cable)
    return correct_cable, clock


def check_cable(e):
    global end
    if end:
        return
    cable = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)[0]
    if correct_cable == cable:
        canvas.create_text(WIDTH//2, 200, text="VYHRAL SI", font="Arial 30 bold")
    else:
        canvas.delete('all')
    end = True


root = tk.Tk()

WIDTH = 500
HEIGHT = 300
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

end = False
time = 11
correct_cable, clock = setup()
timer()
canvas.tag_bind("cable", "<Button-1>", check_cable)

root.mainloop()