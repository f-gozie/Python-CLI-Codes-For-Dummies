# from Tkinter import *
from tkinter import *

def submit():
	contacts = open("Contacts.txt",'a')
	read_contacts = open("Contacts.txt",'r')
	no_of_lines = read_contacts.readlines()
	no_of_lines = len(no_of_lines) + 1
	Details = str(no_of_lines) + " " + name.get() + " 		" + email.get() + " 		" + number.get() + "\n"
	contacts.write(Details)
	name.set('')
	email.set('')
	number.set('')
	
if __name__ == "__main__":

	window = Tk()

	name = StringVar()
	email = StringVar()
	number = StringVar()

	frame = Frame(window)
	frame.pack()

	label_name = Label(frame,text="Name")
	label_name.grid(row=0,column=0)

	entry_name = Entry(frame, textvariable=name)
	entry_name.grid(row=0, column=1)

	label_email = Label(frame,text="email")
	label_email.grid(row=1,column=0)

	entry_email = Entry(frame, textvariable=email)
	entry_email.grid(row=1, column=1)

	label_number = Label(frame,text="Number")
	label_number.grid(row=2,column=0)

	entry_number = Entry(frame, textvariable=number)
	entry_number.grid(row=2, column=1)

	submit_button = Button(frame, text="submit", command=submit)
	submit_button.grid(rowspan=2)


	window.mainloop()