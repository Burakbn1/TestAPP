import os
import sys
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import find_place
import new_page


class resimInsert:
    def __init__(self, dosya_adi, resim_sayisi, resim_url):
        self.dosya_adi= dosya_adi
        self.resim_sayisi= resim_sayisi
        self.resim_url= resim_url
        os.chdir(sys.path[0])
        kullanilan = dosya_adi + '.docx'
        print(kullanilan)
        self.resim_sayisi = resim_sayisi
        self.resim_url = resim_url
        new_page.degisken_atama.resim_url_alma(self, resim_url)
        print("Denetleme noktası1")


    def islem(self):
       
        find_place.find_place_pics(self.dosya_adi, self.resim_sayisi, self.resim_url) 
        find_place.create_place_pic_spot(self.dosya_adi, self.resim_sayisi, self.resim_url)
        print("Deneme Başarılı resim insert islem")    
