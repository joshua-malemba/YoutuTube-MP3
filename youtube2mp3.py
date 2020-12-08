#ALWAYS CAPITALIZE THE T FOR YOUTUBE!!!!!#
from moviepy.editor import *
import moviepy.editor as mp
from pytube import YouTube
from tkinter import messagebox
import os
from tkinter import *
master = Tk()

        
def mp3():
    yt = YouTube(e.get())

    path = '/Users/Bill Malemba/Documents/University/Technologies/PROJECTS'

    audio = yt.streams.filter()

    audio[0].download()

    directory = os.listdir(path)
    
    for file in directory:
    ## issue ----> not read as video object, but str object instead
    ### consider VideoFileClip to read the file as a video object first!
        if file.endswith('.mp4'):
            video = mp.VideoFileClip(file)
            clip = video.audio
            clip.write_audiofile("theaudio.mp3")
            # now delete video since audio now exists !
        else:
            pass
    # video url ----> https://youtu.be/EWaupOupfEUE
    # youtube web-link ----> https://www.youtube.com/watch?v=EWupOupfEUE
def mp4():
    try:
        yt1 = YouTube(e.get())

        path = '/Users/Bill Malemba/Documents/University/Technologies'

        video = yt1.streams.filter()

        video[0].download()
    except ValueError:
        e.delete(0, END)
        messagebox.showinfo('Link Unaccepted! Video URL preferred to Web Link')
    
def check():
    if tkvar.get() == 'MP3':
        mp3()
    elif tkvar.get() == 'MP4':
        mp4()

l = Label(master, text = 'Youtube Link')
l.grid(row=0, column=0)

e = Entry(master)
e.grid(row = 0, column = 1)

tkvar = StringVar()
values = ['MP3', 'MP4']
tkvar.set('MP3')

popMenu = OptionMenu(master, tkvar, *values) # define pop up menu
popMenu.grid(row = 1, column = 0)

b = Button(master, text = 'CONVERT', command=check)
b.grid(row = 0, column = 2)

master.geometry('300x105')

master.title('Joshs Converter')

# think about filedialog.askdirectory() ? 
