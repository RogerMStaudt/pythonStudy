import tkinter as tk
from math import sin, cos, pi;
from datetime import datetime

def draw_clock():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250)

    for i in range(1, 13):
        angle = 90 - i * 30

        x = 150 + 85 * cos(angle * (pi / 180))
        y = 150 - 85 * sin(angle * (pi / 180))

        canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))


def update_pointers():
    time = datetime.now()

    seconds = time.second
    minutes = time.minute
    hours = time.hour

    seconds_angle = 90 - seconds * 6
    minutes_angle = 90 - minutes * 6 - seconds * 0.1
    hours_angle = 90 - (hours * 30 + minutes * 0.5)

    draw_clock()
    
    draw_pointer(150, 150, seconds_angle, 80, 1)
    draw_pointer(150, 150, minutes_angle, 70, 2)
    draw_pointer(150, 150, hours_angle, 50, 4)

    root.after(1000, update_pointers)


def draw_pointer(x, y, angle, length, width):
    radian_angle = angle * (pi / 180)
    end_x = x + length * cos(radian_angle)
    end_y = y - length * sin(radian_angle)

    canvas.create_line(x, y, end_x, end_y, width=width)

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=350, height=350)
canvas.pack()

update_pointers()

root.mainloop()