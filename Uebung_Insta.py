
# Fenster Ausgabe:
#import tkinter as tk
#
# parent=tk.Tk()
#
#parent.title("Welcome to Python.hub")
#
# parent.mainloop()

from tkinter import *
from tkinter import messagebox

win = Tk()

result1 = messagebox.askokcancel("Title1 ", "Do you Really?")
print(result1)

result2 = messagebox.askokcancel("Title2 ", "Do you Really?")
print(result2)

result3 = messagebox.askokcancel("Title3 ", "Do you Really?")
print(result3)

messagebox.showinfo("Title", "a Tk MessageBox")
messagebox.showwarning("warning", "a Tk warning")
messagebox.showerror("error", "a Tk error")

win.mainloop()
