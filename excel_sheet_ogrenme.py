import pandas as pd

def excel_sheet_ogrenme(excel_dosya_konum):

    xls = pd.ExcelFile(excel_dosya_konum)
    sheet_names = xls.sheet_names

    # Sayfa adlarını yazdırma
    print("Available sheets:", sheet_names)

    if('Sayfa1') in sheet_names:
        print("Aranan deger bulundu") 
        
        
####Bu fonksiyonu daha sisteme eklemedik sakın unutma!!###

excel_sheet_ogrenme(r'\\ad001.siemens.net\dfs001\File\TR\SI_DS_TR_RnD\02_Test_Laboratuvari\02_Testler\2024\24-027\01-Gelen\12902782_Goker Yilmaz.xlsx')