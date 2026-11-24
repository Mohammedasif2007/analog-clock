import tkinter as tk
import math
import time

WIDTH = 400
HEIGHT = 400
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 150

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


def draw_clock():
    canvas.delete("all")

    # Outer circle
    canvas.create_oval(
        CENTER_X - RADIUS,
        CENTER_Y - RADIUS,
        CENTER_X + RADIUS,
        CENTER_Y + RADIUS,
        outline="#333333",
        width=4
    )

    # Hour marks
    for i in range(12):
        angle = math.radians(i * 30 - 90)

        x1 = CENTER_X + (RADIUS - 18) * math.cos(angle)
        y1 = CENTER_Y + (RADIUS - 18) * math.sin(angle)

        x2 = CENTER_X + (RADIUS - 5) * math.cos(angle)
        y2 = CENTER_Y + (RADIUS - 5) * math.sin(angle)

        canvas.create_line(x1, y1, x2, y2, fill="white", width=3)

    # Numbers
    nums = {12:0, 3:3, 6:6, 9:9}

    for n, pos in nums.items():
        angle = math.radians(pos * 30 - 90)
        x = CENTER_X + (RADIUS - 32) * math.cos(angle)
        y = CENTER_Y + (RADIUS - 32) * math.sin(angle)

        canvas.create_text(
            x,
            y,
            text=str(n),
            fill="white",
            font=("Georgia", 20, "bold")
        )

    t = time.localtime()

    sec = t.tm_sec
    minute = t.tm_min + sec / 60
    hour = (t.tm_hour % 12) + minute / 60

    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 - 90)

    # Hour hand
    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        CENTER_X + 70 * math.cos(hour_angle),
        CENTER_Y + 70 * math.sin(hour_angle),
        fill="white",
        width=5
    )

    # Minute hand
    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        CENTER_X + 100 * math.cos(min_angle),
        CENTER_Y + 100 * math.sin(min_angle),
        fill="lightgray",
        width=3
    )

    # Second hand
    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        CENTER_X + 115 * math.cos(sec_angle),
        CENTER_Y + 115 * math.sin(sec_angle),
        fill="red",
        width=2
    )

    # Center circle
    canvas.create_oval(
        CENTER_X-5,
        CENTER_Y-5,
        CENTER_X+5,
        CENTER_Y+5,
        fill="white",
        outline=""
    )

    root.after(1000, draw_clock)

draw_clock()
root.mainloop()
