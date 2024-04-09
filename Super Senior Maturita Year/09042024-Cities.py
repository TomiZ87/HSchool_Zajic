import tkinter
import random
tk = tkinter.Canvas(width = 500, height = 500, bg = "silver")
tk.pack()
lines = 1
all_lines1, all_lines2 = [], []
x_c = random.randint(200, 300)
y_c = random.randint(200, 300)
tk.create_oval(x_c-10, y_c-10, x_c+10, y_c+10, fill = "red")
cities = []
def draw_line1(x1, y1, x2, y2):
    global lines
    id = "line" + str(lines)
    tk.create_line(x1, y1, x2, y2, width = 3, tags=["lines", id])
    distance = round(((x2-x1)**2+(y2-y1)**2)**0.5)
    textik = tk.create_text(((x1+x2)/2), ((y1+y2)/2), text=distance, font='arial 15', fill='red', tags=["lines", id])
    bg = tk.create_rectangle(tk.bbox(textik),fill="ivory2", tags="lines")
    tk.tag_lower(bg, textik)
    all_lines1.append(id)
    all_lines2.append(distance)
    lines += 1
def drawing():
    erase()
    global lines
    lines = 1
    for x in range(8):
        draw_line1(x_c, y_c, cities[x][0], cities[x][1])
def erase():
    global lines, all_lines1, all_lines2
    tk.delete('lines')
    all_lines1, all_lines2 = [], []
    lines = 1
def minmax():
    global x_c, y_c
    if len(all_lines1) == len(cities) and len(all_lines2) == len(cities):  
        max_distance = max(all_lines2) 
        max_distance_line = all_lines1[all_lines2.index(max_distance)]
        min_distance = min(all_lines2) 
        min_distance_line = all_lines1[all_lines2.index(min_distance)]
        x1, y1 = cities[all_lines2.index(max_distance)][0], cities[all_lines2.index(max_distance)][1]
        x2, y2 = cities[all_lines2.index(min_distance)][0], cities[all_lines2.index(min_distance)][1]
    else:
        dist = []
        for x in range(8):
            x1, y1, x2, y2 = cities[x][0], cities[x][1], x_c, y_c
            distance = round(((x2-x1)**2+(y2-y1)**2)**0.5)
            dist.append(distance)
        max_distance = max(dist)
        max_distance_line = "line" + str(dist.index(max_distance))
        min_distance = min(dist)
        min_distance_line = "line" + str(dist.index(min_distance))
        x1, y1 = cities[dist.index(max_distance)][0], cities[dist.index(max_distance)][1]
        x2, y2 = cities[dist.index(min_distance)][0], cities[dist.index(min_distance)][1]

    tk.create_line(x_c, y_c, x1, y1, width = 3, tags=["lines", max_distance_line], fill="red")
    textik1 = tk.create_text(((x1+x_c)/2), ((y1+y_c)/2), text=max_distance, font='arial 20', fill='lawn green', tags=["lines", max_distance_line])
    bg1 = tk.create_rectangle(tk.bbox(textik1),fill="ivory2", tags=["lines", max_distance_line])
    tk.tag_lower(bg1, textik1)
    tk.create_line(x_c, y_c, x2, y2, width = 3, tags=["lines", min_distance_line], fill="red")
    textik2 = tk.create_text(((x2+x_c)/2), ((y2+y_c)/2), text=min_distance, font='arial 20', fill='lawn green', tags=["lines", min_distance_line])
    bg2 = tk.create_rectangle(tk.bbox(textik2),fill="ivory2", tags=["lines", min_distance_line])
    tk.tag_lower(bg2, textik2)
def onclick(event):
    city = tk.find_closest(event.x, event.y)
    coordinates = tk.coords(city)
    x2 = coordinates[0]
    y2 = coordinates[1]
    dolines = False
    for x in city:
        if "village" in tk.gettags(x):
            dolines = True
            x2 = x2 + 4
            y2 = y2 + 4
        elif "city" in tk.gettags(x):
            dolines = True
            x2 = x2 + 7
            y2 = y2 + 7
    if dolines:
        distance = round(((x2-x_c)**2+(y2-y_c)**2)**0.5)
        tk.create_line(x_c, y_c, x2, y2, width = 3, tags=["lines", "temp"], fill="red")
        textik2 = tk.create_text(((x2+x_c)/2), ((y2+y_c)/2), text=distance, font='arial 15', fill='red', tags=["lines", "temp"])
        bg2 = tk.create_rectangle(tk.bbox(textik2),fill="ivory2", tags=["lines", "temp"])
        tk.tag_lower(bg2, textik2)
for z in range(3):
    while True:
        x = random.randint(14, 486)
        y = random.randint(14, 486)
        if (abs(x_c-x) > 39) and (abs(y_c-y) > 39):
            labeling = "M" + str(z+1)
            tk.create_oval(x-7, y-7, x+7, y+7, fill = "blue", tags="city")
            tk.create_text (x, y-15, text=labeling, font='arial 10', fill='black') 
            cities.append([x, y])
            break
for z in range(5):
    while True:
        x = random.randint(8, 492)
        y = random.randint(8, 492)
        if (abs(x_c-x) > 39) and (abs(y_c-y) > 39):
            labeling = "D" + str(z+1)
            tk.create_oval(x-4, y-4, x+4, y+4, fill = "green", tags="village")
            tk.create_text (x, y-10, text=labeling, font='arial 10', fill='black')
            cities.append([x, y])
            break
button_1 = tkinter.Button(text="Delete All", command=erase)
button_1.pack()
button_2 = tkinter.Button(text="Draw", command=drawing)
button_2.pack()
button_3 = tkinter.Button(text="Min/Max", command=minmax)
button_3.pack()
tk.bind('<Button-1>', onclick)
tk.mainloop()