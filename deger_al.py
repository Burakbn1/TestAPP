import tkinter
import customtkinter
from PIL import Image, ImageTk

def degerleri_al_func():
    dialog = customtkinter.CTkInputDialog(text="Dosya Göndermek İstediğiniz Server Yolunu Giriniz:", title="DosyaKayıtYolu")
    dosya_kayit_yolu= dialog.get_input()
