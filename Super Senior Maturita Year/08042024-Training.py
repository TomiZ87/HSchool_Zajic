import tkinter
import random
tk = tkinter.Canvas(width=500, height=500, bg="silver")
tk.pack()
coord = []

def circle(coordinates):
    x = coordinates.x
    y = coordinates.y
    tk.create_oval(x-10, y-10, x+10, y+10, fill="red")
    if coordinates.num == 3: 
        f = open("./Super Senior Maturita Year/files/08042024-Training.txt", "a", encoding="utf-8")
        f.write(str(x) + " " + str(y) + "\n")
        f.close()
        coord.append([x, y])

def circlerandom():
    x = random.randint(10, 490)
    y = random.randint(10, 490)
    tk.create_oval(x-10, y-10, x+10, y+10, fill="red")
    

def rectanglerandom():
    x = random.randint(10, 490)
    y = random.randint(10, 490)
    tk.create_rectangle(x, y, x+10, y+10, fill="blue")

def rectangle(coordinates):
    x = coordinates.x
    y = coordinates.y
    tk.create_rectangle(x, y, x+10, y+10, fill="blue")
    if coordinates.num == 1: 
        f = open("./Super Senior Maturita Year/files/08042024-Training.txt", "a", encoding="utf-8")
        f.write(str(x) + " " + str(y) + "\n")
        f.close()
        coord.append([x, y])

def erase(coor=None):
    tk.delete('all')

circlerandom()
rectanglerandom()
tk.bind("<Button-3>", circle, "Mod1")
tk.bind("<B3-Motion>", circle, "Mod2")
tk.bind("<Button-1>", rectangle)
tk.bind("<B1-Motion>", rectangle)
tk.bind("<Button-2>", erase)
button_1 = tkinter.Button(text="Circle", command=circlerandom)
button_1.pack()
button_2 = tkinter.Button(text="Delete All", command=erase)
button_2.pack()

tk.mainloop()