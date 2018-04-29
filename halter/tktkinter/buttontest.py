from tkinter import Tk, Button

count = 0  # Initialize the counter that records the number of button presses


def update():
    """
    Updates the count label within the graphical button
    :return: count
    """
    global count, b
    count += 1
    b.config(text="Click count = " + str(count))
    print("Updating")


window = Tk()
b = Button(window)
b.configure(background='blue', text='Click count = 0', command=update)
b.pack()
window.mainloop()