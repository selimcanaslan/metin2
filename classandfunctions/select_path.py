from tkinter import filedialog
from tkinter import *


def path():
    global folder_selected
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected