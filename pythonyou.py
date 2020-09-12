from tkinter import *
import pytube
win=Tk()
win["bg"]=("white")

def down():
	print(link.get)
	url = link.get()
	youtube = pytube.YouTube (url)
	video = youtube.streams.get_highest_resolution()
	video.download("/storage/emulated/0/bluetooth")
	print('done')

lbl=Label(win,text="You Tube Downloader",bg="#ff1a1a",fg="white",font="Helvetica 10 bold")
lbl.place(x=180,y=100)

lbl1=Label(win,text="Video Link",fg="white",bg="#ff1a1a")
lbl1.place(x=100,y=200)

link=Entry(win,bg="#ff1a1a",fg="white")
link.place(x=250,y=200)

	

button=Button(win,text="Download",bg="#ff1a1a",fg="#ffffff",activebackground="#ff1a1a",command=down)
button.place(x=250,y=300)


win.mainloop()