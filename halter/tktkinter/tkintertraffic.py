from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame


def do_button_press():
    """
    The window manager will call this function when the user
    calls the graphical button. The variables, color, canvas,
    red_lamp, yellow_lamp and green_lamp are global variables
    that this function expects to exist.
    """
    global color
    if color == 'red':
        color == 'green'
        canvas.itemconfigure(red_lamp, fill='black')
        canvas.itemconfigure(green_lamp, fill='green')
    elif color == 'green':
        color = 'yellow'
        canvas.itemconfigure(green_lamp, fill='black')
        canvas.itemconfigure(yellow_lamp, fill='yellow')
    elif color == 'yellow':
        color = 'red'
        canvas.itemconfigure(yellow_lamp, fill='black')
        canvas.itemconfigure(red_lamp, fill='red')

color = 'red'
window = Tk()
window.title("Agozie is awesome")

frame = Frame(window)
frame.pack()

canvas = Canvas(frame, width=150, height=300)

canvas.create_rectangle(50, 20, 150, 280, fill='gray')

red_lamp = canvas.create_oval(70, 40, 130, 100, fill='red')

yellow_lamp = canvas.create_oval(70, 200, 130, 260, fill='black')

green_lamp = canvas.create_oval(70, 120, 130, 180, fill='black')

button = Button(frame, text='Change', command=do_button_press)


button.grid(row=0, column=0)
canvas.grid(row=0, column=1)

window.mainloop()
