from tkinter import messagebox as mb
import tkinter as tk
def hide(root):
    root.withdraw()

def succeed():
    root = tk.Tk()
    hide(root)
    mb.showinfo("HESAPLAMA BAŞARILI !", "Verileriniz Hesaplanmıştır!",)