from Tkinter import *

window = Tk()

def submit():
	a = str(artist)
	b = str(age)
	c = str(song)
	d = str(album)
	with open('file_examples/input.txt','a') as Artist:


artist = StringVar()
age = IntVar()
song = StringVar()
album = StringVar()

frame = Frame(window)
frame.pack()

artist_label = Label(frame,text='Who is your favorite artist?')
artist_label.grid(row=0,column=0)
artist_entry = Entry(frame,textvariable=artist)
artist_entry.grid(row=0,column=1)

age_label = Label(frame,text='Who is your favorite artist?')
age_label.grid(row=1,column=0)
age_entry = Entry(frame,textvariable=artist)
age_entry.grid(row=1,column=1)

song_label = Label(frame,text='Favorite Song?')
song_label.grid(row=2,column=0)
song_entry = Entry(frame,textvariable=song)
song_entry.grid(row=2,column=1)

album_label = Label(frame,text='Who is your favorite artist?')
album_label.grid(row=3,column=0)
album_entry = Entry(frame,textvariable=artist)
album_entry.grid(row=3,column=1)

button = Button(frame,text="Submit",command=submit)
button.grid(rowspan=2)