import tkinter
window = tkinter.Tk()
lbl = tkinter.Label(window, text = 'Enter your Name')
lbl.pack({'side':'top'})
name = tkinter.Entry(window)
name.pack({'side':'top'})

btnsubmit = tkinter.Button(window, text = 'Submit', command = 'submitForm')
btnsubmit.pack({'side':'top', 'pady':20})
window.mainloop()