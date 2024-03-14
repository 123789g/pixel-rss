from tkinter import *
from PIL import Image, ImageTk

# This class recreates functionality for our window. In particular, the ability to click and drag the window.
class customTitleBar(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.on_drag)

    def start_drag(self, event):
        self._drag_start_x = event._drag_start_x
        self._drag_start_y = event._drag_start_y

    def on_drag(self, event):
        x = self.master.winfo_x() + event.x - self._drag_start_x
        y = self.master.winfo_y() + event.y - self._drag_start_y
        self.master.geometry(f"+{x}+{y}")

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

root.mainloop()