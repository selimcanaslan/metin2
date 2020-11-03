from tkinter import messagebox as mb
import tkinter as tk


def hide(root):
    root.withdraw()


def error():
    root = tk.Tk()
    hide(root)
    mb.showerror("Hatasız Kul Olmaz !", " Hacı var bir yanlışın", )
