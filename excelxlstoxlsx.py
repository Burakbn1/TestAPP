import os, sys
from win32com.client import DispatchEx
import pythoncom


def convert_xls_to_xlsx(self, xls_file_path):
    global xlsx_file_path
    pythoncom.CoInitialize()  # COM başlatma
    file_path= os.path.dirname(os.path.abspath(sys.argv[0])) 
    gelenad= "\\bom_excell.xlsx"
    print("xls_file_path="+ xls_file_path)
    if os.path.isdir(file_path)== False:
        os.mkdir("excel_xlsx_file")
    else:
        print("Dosya mevcut")
    
    #xlsx_file_konum= file_path + "\\excel_xlsx_file"
    xlsx_file_path= file_path+ "\\excel_xlsx_file"+ gelenad
    self.xlsx_file_path= xlsx_file_path

    excel_app = DispatchEx("Excel.Application")
    print("Excel Application başlatıldı")

    workbook = None

    try:
        # Excel dosyasını read-only modda aç
        workbook = excel_app.Workbooks.Open(xls_file_path, ReadOnly=True)
        print("Workbook açıldı")

        # .xlsx formatında kaydet
        workbook.SaveAs(xlsx_file_path, FileFormat=51)  # 51 = xlsx formatı
        print(f"{xls_file_path} dosyası başarıyla {xlsx_file_path} dosyasına dönüştürüldü.")
        

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

    

def get_variable_from_func():
    
    return xlsx_file_path

