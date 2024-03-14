from tkinter import *
from PIL import Image, ImageTk

# This class recreates functionality for our window. In particular, the ability to click and drag the window.
class customTitleBar(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

def start_drag(event):
    root._drag_start_x = event.x_root - root.winfo_x()
    root._drag_start_y = event.y_root - root.winfo_y()

def on_drag(event):
    new_x = event.x_root - root._drag_start_x
    new_y = event.y_root - root._drag_start_y
    root.geometry(f"+{new_x}+{new_y}")

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
maximizeButton = Button(titlebar, image=maximizeImg, borderwidth=0, bg="#363636")
maximizeButton.pack(side="right")
minimizeButton = Button(titlebar, image=minimizeImg, borderwidth=0, bg="#363636")
minimizeButton.pack(side="right")

titlebar.bind("<ButtonPress-1>", start_drag)
titlebar.bind("<B1-Motion>", on_drag)

root.mainloop()