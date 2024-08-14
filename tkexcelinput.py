import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import excelxlstoxlsx

class ExcelDropApp(TkinterDnD.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Drag and Drop Excel App")
        self.geometry("800x600")

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Drag and drop Excel files here", width=40, height=10, fg_color='green')
        self.label.pack(padx=20, pady=20, fill="both", expand=True)

        # Register the label as a drop target
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.drop)

        self.input_alindi= False

        self.file_paths = []  # List to store file paths

        self.button = ctk.CTkButton(self.frame, text="Gönder", command=self.buttoncallback)
        self.button.pack(padx=10, pady=10, side=ctk.BOTTOM)
        #print(self.button)
        # Butonu en öne getirme
        self.button.lift()
        #return self.input_alindi

    def buttoncallback(self):
        print("Converting files...")
        app = ctk.CTk()
        app.destroy()
        for file_path in self.file_paths:
            if file_path.lower().endswith('.xls') or file_path.lower().endswith('xlsx'):
                xlsx_file_path= excelxlstoxlsx.convert_xls_to_xlsx(self,file_path)
                break

            else:
                print(f"Skipping non-xls file: {file_path}")
        print("Excel conversion complete")
        app.quit()
        

    def drop(self, event):
        # Get the file paths of the dropped files
        file_paths = self.tk.splitlist(event.data)
        for file_path in file_paths:
            if file_path.lower().endswith(('.xls', '.xlsx')):
                self.file_paths.append(file_path)  # Add file path to the list
                print(f"Accepted file: {file_path}")
            else:
                print(f"Rejected file: {file_path}")
        print(self.file_paths)  # Print all accepted file paths

    
    
if __name__ == "__main__":
    app = ExcelDropApp()
    app.mainloop()