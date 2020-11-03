from tkinter import messagebox as mb
import tkinter as tk
def hide(root):
    root.withdraw()

def file_created():
    root = tk.Tk()
    hide(root)
    mb.showinfo("Log Dosyası Bulunamadı !", "log.txt Oluşturuldu !\nHesapla Butonuna Tekrar Basınız",)