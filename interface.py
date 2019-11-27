from tkinter import *
from PIL import ImageTk, Image
import os


class Application:
    def __init__(self, master=None):
        self.frame = Frame(master)
        self.frame.pack()

        #self.img = ImageTk.PhotoImage(Image.open("testeArea.jpeg"))
        #self.panel = Label(self.frame, image = self.img)
        #self.panel.pack(side = "bottom", fill = "both", expand = "yes")

        self.txt = Label(self.frame,text="oiiiiiiiii")
        self.txt.pack()

root = Tk()
Application(root)
root.mainloop()

