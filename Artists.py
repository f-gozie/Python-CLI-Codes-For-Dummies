from Tkinter import *

window = tkinter.Tk()

def submit():
	a = str(artist.get())
	b = str(age.get())
	c = str(song.get())
	d = str(album.get())
	with open('input.txt','a') as Artist:
		new_line = 'Artist: {0} \n Age: {1} \n Song: {2} \n Album: {3} \n \n'.format(a,b,c,d)
		Artist.write(new_line)

	artist.set('')
	age.set(0)
	song.set('')
	album.set('')


artist = StringVar()
age = IntVar()
song = StringVar()
album = StringVar()

frame = Frame(window)
frame.pack()

artist_label = Label(frame,text='Artist?', font='bold')
artist_label.grid(row=0,column=0)
artist_entry = Entry(frame,textvariable=artist,font='bold')
artist_entry.grid(row=0,column=1)

age_label = Label(frame,text='Age?',font='bold')
age_label.grid(row=1,column=0)
age_entry = Entry(frame,textvariable=age,font='bold')
age_entry.grid(row=1,column=1)

song_label = Label(frame,text='Artist Song?',font='bold')
song_label.grid(row=2,column=0)
song_entry = Entry(frame,textvariable=song,font='bold')
song_entry.grid(row=2,column=1)

album_label = Label(frame,text='Album?',font='bold')
album_label.grid(row=3,column=0)
album_entry = Entry(frame,textvariable=album,font='bold')
album_entry.grid(row=3,column=1)

button = Button(frame,text="Submit",command=submit,font='bold')
button.grid(rowspan=4)

window.mainloop()
