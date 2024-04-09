import tkinter
tk = tkinter.Canvas(width = 500, height = 500, bg = "silver")
tk.pack()
file = open("./Super Senior Maturita Year/files/09042024-Lines.txt", "r")
for x in file.readlines():
    coordinates = x.split(" ")
    tk.create_line(coordinates[0], coordinates[1], coordinates[2], coordinates[3], width = 3)
file.close()
tk.mainloop()