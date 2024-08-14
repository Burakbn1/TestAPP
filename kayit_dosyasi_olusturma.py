import os, sys
import control_json

def create_save_file(proje_adi):

    global current_directory

    current_directory = os.getcwd()

    global dosya_konumu

    dosya_konumu = control_json.deger_oku()
    print(dosya_konumu)

    global ana_dosya_adi

    ana_dosya_adi = "TestDosyalari"

    global ana_dosya_yolu

    ana_dosya_yolu= "/" + ana_dosya_adi

    global glob_proje_adi, form_dosya_konumu, proje_dosya_konumu, proje_adi_konum

    glob_proje_adi = proje_adi

    proje_adi_konum= "/"+ proje_adi

    form_dosya_konumu= dosya_konumu + ana_dosya_adi

    proje_dosya_konumu = form_dosya_konumu + proje_adi_konum

    global ekran_alintilari_dosya_konum

    ekran_alintilari_dosya_konum= proje_dosya_konumu + "/" +glob_proje_adi + "_ekran_alintilari"

    global pdf_file_konumu

    pdf_file_konumu= proje_dosya_konumu + "/" + proje_adi + ".pdf"
    print(pdf_file_konumu)
    print(ekran_alintilari_dosya_konum)

    os.chdir(dosya_konumu)

    sorgulanacak_konum= dosya_konumu+ ana_dosya_yolu

    if os.path.isdir(sorgulanacak_konum)== False:
        
        os.mkdir(ana_dosya_adi)
        
    else:
        print("Dosya mevcut")
        
    create_project_file(proje_adi)
        
    #return sorgulanacak_konum


def create_project_file(proje_adi):

    os.chdir(form_dosya_konumu)

    if os.path.isdir(proje_adi)== False:
        
        os.mkdir(proje_adi)
        #os.chdir(dosya_konumu+proje_adi_konum)
        #print(os.getcwd())
        print("Proje Dosyası Başarı ile Oluşturuldu.")
        

    else:
        print("Bu proje ismi zaten mevcut. Lütfen başka bir isim seçin")

    create_pic_save_file()

def create_pic_save_file():

    os.chdir(proje_dosya_konumu)

    ekran_alintilari_dosya= glob_proje_adi + "_ekran_alintilari"

    if os.path.isdir(ekran_alintilari_dosya)== False:
        
        os.mkdir(ekran_alintilari_dosya)
        #os.chdir(dosya_konumu+proje_adi_konum)
        #print(os.getcwd())
        print("Proje Dosyası Başarı ile Oluşturuldu.")
        os.chdir(current_directory)
        

    else:
        print("Bu proje ismi zaten mevcut. Lütfen başka bir isim seçin")
        os.chdir(current_directory)

path= r"C:/"



#create_save_file("221204085")


