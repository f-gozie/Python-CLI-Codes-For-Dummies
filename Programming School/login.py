from Tkinter import *
from signup import *
import sqlite3

con = sqlite3.connect('Users.db')
cur = con.cursor()
cur.execute('SELECT * FROM Users')
content = cur.fetchall()

def login():
	for i in content:
		for j in i:
			if j == name.get():
				a = i
	a = i
	if a[1] == password.get():
		return_type.set('Correct Password')
	else:
		return_type.set('Incorrect Credentials')
		name.set('')
		password.set('')
		return 1
		login()

		

if __name__ == '__main__':	
	window = Tk()
	
	name = StringVar()
	return_type = StringVar()
	password = StringVar()
	password1 = StringVar()
	bank_balance = IntVar()

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

	password_entry = Entry(login_frame,textvariable = password, show="*")
	password_entry.grid(row=1, column=1)

	label = Label(login_frame,textvariable=return_type)
	label.grid(row=2,column=0)	

	login_button = Button(login_frame, text = "Login", command=login)
	login_button.grid(rowspan=2)

	window.mainloop()