import os
from win32com.client import DispatchEx
import pythoncom

def save_single_sheet_as_pdf(file_path, output_pdf_path, sheet_name):
    pythoncom.CoInitialize()  # COM başlatma
    excel_app = DispatchEx("Excel.Application")
    print("Excel to Pdf başlatıldı")
    
    workbook = None

    try:
            workbook = excel_app.Workbooks.Open(file_path, ReadOnly=True)
            print("Workbook açıldı")

            # Belirli bir sayfayı seçip PDF olarak kaydet
            print("2."+ output_pdf_path)
            worksheet = workbook.Sheets(sheet_name)
            worksheet.ExportAsFixedFormat(0, output_pdf_path)
            print(f"{sheet_name} sayfası PDF olarak kaydedildi: {output_pdf_path}")

    except Exception as e:
        import traceback
        print(f"Bir hata oluştu: {e}")
        print(traceback.format_exc())

    finally:
        if workbook:
            workbook.Close(False)
        if excel_app:
            excel_app.Quit()
        pythoncom.CoUninitialize()  # COM kapatma
        
    

    

# Fonksiyonu çağırma
#input_excel_path = r"C:\Users\z004ytzh\Desktop\Projeler\totalproject\excel_xlsx_file\bom_excell.xlsx"
#output_pdf_path = r"C:\Users\z004ytzh\Desktop\Projeler\totalproject\bom_excell.pdf"
#sheet_name = "BOM_EXCHANGE"  # PDF olarak kaydetmek istediğiniz sayfanın adı

#save_single_sheet_as_pdf(input_excel_path, output_pdf_path, sheet_name)
