import tkinter
tk = tkinter.Canvas(width = 500, height = 500, bg = "silver")
tk.pack()
done = 0
coordinates_red = []
coordinates_green = []

def save(mat):
    f = open("./Super Senior Maturita Year/files/09042024-DistanceLine.txt", "a", encoding='utf-8')
    f.write(mat)
    f.close()

def draw_line():
    global done
    if len(coordinates_green) > done and len(coordinates_red) > done:
            tk.create_line(coordinates_red[done][0], coordinates_red[done][1], coordinates_green[done][0], coordinates_green[done][1], width = 3)
            save(str(coordinates_red[done][0]) + " " + str(coordinates_red[done][1]) + " " + str(coordinates_green[done][0]) + " " + str(coordinates_green[done][1]) + "\n")
            distance = round(((coordinates_red[done][0]-coordinates_green[done][0])**2+(coordinates_red[done][1]-coordinates_green[done][1])**2)**0.5)
            tk.create_text(((coordinates_red[done][0]+coordinates_green[done][0])/2), ((coordinates_red[done][1]+coordinates_green[done][1])/2), text=distance, font='arial 15', fill='blue')
            done += 1

def circle(coordinates):
    coordinates_red.append([coordinates.x, coordinates.y])
    tk.create_oval(coordinates.x-5, coordinates.y-5, coordinates.x+5, coordinates.y+5, fill = "red")
    draw_line()

def circle2(coordinates):
    coordinates_green.append([coordinates.x, coordinates.y])
    tk.create_oval(coordinates.x-5, coordinates.y-5, coordinates.x+5, coordinates.y+5, fill = "green")
    draw_line()

def erase():
    tk.delete('all')
    global done, coordinates_red, coordinates_green
    done = 0
    coordinates_red = []
    coordinates_green = []
    
button_1 = tkinter.Button(text="Delete All", command=erase)
button_1.pack()

tk.bind("<Button-1>", circle)
tk.bind("<Button-3>", circle2)
tk.mainloop()