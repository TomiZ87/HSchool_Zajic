import tkinter
import random
colors = ['red', 'yellow', 'blue', 'green']
while True:
    own_color = input("Color: ")
    if own_color in colors:
        own_number = input("Numbers: ")
        try:
            own_number = int(own_number)
            if 0 < own_number and own_number < 10:
                break
        except ValueError: print("Try again")
window = tkinter.Tk()
canvas = tkinter.Canvas(width = 1500, height = 320, bg = 'gray')
canvas.pack()
canvas.create_rectangle (10, 10, 210, 310, fill='white', outline='black', width=3)
canvas.create_oval (20, 20, 80, 80, fill=own_color)
canvas.create_oval (140, 240, 200, 300, fill=own_color)
canvas.create_text (50, 50, text=own_number, font='arial 25', fill='black')
canvas.create_text (170, 270, text=own_number, font='arial 25', fill='black')
canvas.create_rectangle (35, 125, 185, 195, fill='black')
canvas.create_text (110, 160, text='BILGYM', font='arial 25', fill=own_color)  
positions = 210
for x in range(5):
    color = random.choice(colors)
    number = random.randint(1, 9)
    canvas.create_rectangle (10 + positions, 10, 210 + positions, 310, fill='white', outline='black', width=3)
    canvas.create_oval (20 + positions, 20, 80 + positions, 80, fill=color)
    canvas.create_oval (140 + positions, 240, 200 + positions, 300, fill=color)
    canvas.create_text (50 + positions, 50, text=number, font='arial 25', fill='black')
    canvas.create_text (170 + positions, 270, text=number, font='arial 25', fill='black')
    canvas.create_rectangle (35 + positions, 125, 185 + positions, 195, fill='black')
    canvas.create_text (110 + positions, 160, text='BILGYM', font='arial 25', fill=color)
    positions += 210
window.mainloop()