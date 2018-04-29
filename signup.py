from Tkinter import *
# from login import *

def sign_up():
	name.set('')
	password.set('')
	password1.set('')
	bank_balance.set(0)


if __name__ == '__main__':
	window = Tk()

	name = StringVar()
	password = StringVar()
	password1 = StringVar()
	bank_balance = IntVar()

	sign_up_frame = Frame(window)
	sign_up_frame.pack()


	name_label = Label(sign_up_frame, text="UserName")
	name_label.grid(row=0, column=0)

	name_entry = Entry(sign_up_frame,textvariable = name)
	name_entry.grid(row=0, column=1)

	password_label = Label(sign_up_frame, text="Password")
	password_label.grid(row=1, column=0)

	password_entry = Entry(sign_up_frame,textvariable = password, show="*")
	password_entry.grid(row=1, column=1)

	password1_label = Label(sign_up_frame, text="Password again")
	password1_label.grid(row=2, column=0)

	password1_entry = Entry(sign_up_frame,textvariable = password1, show="*")
	password1_entry.grid(row=2, column=1)

	bank_balance_label = Label(sign_up_frame, text="Bank Balance")
	bank_balance_label.grid(row=3, column=0)

	bank_balance_entry = Entry(sign_up_frame,textvariable = bank_balance)
	bank_balance_entry.grid(row=3, column=1)

	sign_up_button = Button(sign_up_frame, text = "sign up", command=sign_up)
	sign_up_button.grid(rowspan=2)

	window.mainloop()

