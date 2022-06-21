from tkinter import *
from tkinter.ttk import *


window = Tk()
window.wm_title("Softy Object Editor")

preview = Canvas(name="preview", width=640, height=640, background="#000")
preview.pack()

mass = Entry()

window.mainloop()
