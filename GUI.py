from Tkinter import *

def login():
	name.set(' ')
	password.set(' ')

if __name__ == '__main__':	
	window = Tk()

	name = StringVar()
	password = StringVar()

	login_frame = Frame(window)
	login_frame.pack()

	logged_in_frame = Frame(window)
	logged_in_frame.pack()
	
	name_label = Label(login_frame, text="UserName")
	name_label.grid(row=0, column=0)

	name_entry = Entry(login_frame,textvariable = name)
	name_entry.grid(row=0, column=1)

	password_label = Label(login_frame, text="Password")
	password_label.grid(row=1, column=0)

	name_entry = Entry(login_frame,textvariable = password)
	name_entry.grid(row=1, column=1)

	login_button = Button(login_frame, text = "Login", command=login)
	login_button.grid(rowspan=2)

	window.mainloop()