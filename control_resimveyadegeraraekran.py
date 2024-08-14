import os, sys
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkexcelinput
import converter_excelltopdf
import pdftojpg 
import excelxlstoxlsx 
import deger_alma_ilk_sayfa
import kayit_dosyasi_olusturma



class control_resimveyadegeraraekran(TkinterDnD.Tk):

    def control_araekran(*gelen_array):
        print("control_resimveyadegeraraekran")
        if(gelen_array[0][0] == 0):
            print("manual giriş ekranı çalıştır.")
        elif(gelen_array[0][0] == 1):
            print("resimli giriş ekranı çalıştır.")

        if(gelen_array[0][1] == 0):
            print("manual giriş ekranı çalıştır.")
        elif(gelen_array[0][1] == 1):
            print("resimli giriş ekranı çalıştır.")

        if(gelen_array[0][2] == 0):
            print("manual giriş ekranı çalıştır.")
        elif(gelen_array[0][2] == 1):
            print("resimli giriş ekranı çalıştır.")


        