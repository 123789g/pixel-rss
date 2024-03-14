from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.overrideredirect(True)
root.configure(background="#363636")
root.minsize(960, 720)
root.geometry("800x500")

# Titlebar Customization
closeIcon = Image.open("icons/Close.png")
maximizeIcon = Image.open("icons/Maximize.png")
minimizeIcon = Image.open("icons/Minimize.png")
closeImg = ImageTk.PhotoImage(closeIcon)
maximizeImg = ImageTk.PhotoImage(maximizeIcon)
minimizeImg = ImageTk.PhotoImage(minimizeIcon)

titlebar = Frame(root, bg="#363636", relief="flat", height=25)
titlebar.pack(side="top", fill="x")

closeButton = Button(titlebar, image=closeImg, command=root.destroy, borderwidth=0, bg="#363636")
closeButton.pack(side="right")

root.mainloop()