import os, sys
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkexcelinput
import converter_excelltopdf
import pdftojpg 
import excelxlstoxlsx 
import deger_alma_ilk_sayfa
import kayit_dosyasi_olusturma



class dosya_kontrol(TkinterDnD.Tk):

    def excell_kontrol():
        #output_pdf_path = r"C:\Users\z004ytzh\Desktop\Projeler\totalproject\bom_excell.pdf"
        saving_folder= kayit_dosyasi_olusturma.ekran_alintilari_dosya_konum
        print("merhaba")
        excel_cagir= tkexcelinput.ExcelDropApp()
        excel_cagir.mainloop()
        print("DosyaKontrol Checkpoint Mainloop Çıkış")
        excel_path= excelxlstoxlsx.get_variable_from_func()
        print("DosyaKontrol Checkpoint Excellxlstoxlsx "+ excel_path)
        sheet_name= deger_alma_ilk_sayfa.istenen_deger_don()
        pdf_file_konum= kayit_dosyasi_olusturma.pdf_file_konumu

        #print(output_pdf_path + sheet_name)

        print("DosyaKontrol Checkpoint Outputpdfpath, sheetname")
        print(pdf_file_konum)

        converter_excelltopdf.save_single_sheet_as_pdf(excel_path, pdf_file_konum, sheet_name)
        pdftojpg.pdf2img(pdf_file_konum, saving_folder)
    
        print("input alındı sıfır değil")

    excell_kontrol()