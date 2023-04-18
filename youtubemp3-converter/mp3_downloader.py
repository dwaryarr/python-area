from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
import os

# creates the window using Tk() function
window = Tk()
# creates title for the window
window.title('MP3 Downloader')
# the icon for the application, this will replace the default tkinter icon
# window.iconbitmap(window, 'assets/favicon.ico')
# dimensions and position of the window
window.geometry('500x400+430+180')
# makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)

"""Styles for the widgets"""
# style for the label
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 15))
# style for the entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# style for the button
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')

 # loading the MP3 logo
logo = PhotoImage(file='logo.png')
# creates dimensions for the logo
logo = logo.subsample(2, 2)
# adding the logo to the canvas
canvas.create_image(180, 80, image=logo)
# the Downloader label just next to the logo
mp3_label = ttk.Label(window, text='Downloader', style='TLabel')
canvas.create_window(340, 125, window=mp3_label)

# creates the canvas for containing all the widgets
canvas = Canvas(window, width=500, height=400)
canvas.pack()
# this runs the app infinitely
window.mainloop()
