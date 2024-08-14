from pdf2image import convert_from_path
from tkinter import messagebox
import os
from PIL import Image
import img_rotate

def pdf2img(pdf_path, saving_folder):
    
    poppler_path= r"C:\Release-24.02.0-0\poppler-24.02.0\Library\bin"#url koyacaksan r koy başa
    #pdf_path= r"C:\Users\z004ytzh\Desktop\Projeler\totalproject\bom.pdf"
    print(pdf_path)
    pages= convert_from_path(pdf_path= pdf_path, poppler_path= poppler_path)
    #saving_folder= r"C:\Users\z004ytzh\Desktop\Projeler\totalproject\bomresimler"
    c=1
    for page in pages:
        img_name= f"img-{c}.jpeg"
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        img_path = os.path.join(saving_folder, img_name)
        with Image.open(img_path) as img:
            genislik, yukseklik = img.size
        if genislik > yukseklik:
            print(c)
            img_rotate.image_rotate(img_path)
        # Boyutları yazdırma
        print(f"Eni: {genislik} piksel")
        print(f"Boyu: {yukseklik} piksel")

        c+=1

#pdf2img()