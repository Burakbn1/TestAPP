import customtkinter
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import os, sys
import tkresiminput
import entity_gelen_degerler

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.gelendosya = 'aTempRise.docx'
        self.dosyaadi = "yenibirdosya"
        os.chdir(sys.path[0])
        self.doc = DocxTemplate(self.gelendosya)

        # configure window
        self.title("Siemens Test App")
        self.geometry(f"{1100}x700")

        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.exit_fullscreen)
        self.bind("<Configure>", self.on_resize)

        self.original_image = Image.open("Siemens.jpg")
        self.background_photo = ImageTk.PhotoImage(self.original_image)

        # Create a Canvas
        self.canvas = customtkinter.CTkCanvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Add the image to the Canvas
        self.background_id = self.canvas.create_image(0, 0, image=self.background_photo, anchor='nw')

        # Create a frame on top of the canvas to hold the UI elements
        self.ui_frame = customtkinter.CTkFrame(self.canvas, corner_radius=0, fg_color="black")
        self.ui_frame.pack(fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.ui_frame, anchor='nw')

        # Grid configuration
        self.ui_frame.grid_columnconfigure(0, weight=1)
        self.ui_frame.grid_columnconfigure(1, weight=1)
        self.ui_frame.grid_rowconfigure(0, weight=1)

        # UI Elements
        self.label = customtkinter.CTkLabel(master=self.ui_frame, text="Beklenen Degerler", font=("Roboto", 24), fg_color="transparent")
        self.entry_testno = customtkinter.CTkEntry(self.ui_frame, placeholder_text="TestNo")
        self.entry_reportno = customtkinter.CTkEntry(self.ui_frame, placeholder_text="ReportNo")
        self.entry_typeTest = customtkinter.CTkEntry(self.ui_frame, placeholder_text="TypeTest")
        self.entry_manufacturer = customtkinter.CTkEntry(self.ui_frame, placeholder_text="Manufacturer")
        self.entry_client = customtkinter.CTkEntry(self.ui_frame, placeholder_text="Client")
        self.entry_testobject = customtkinter.CTkEntry(self.ui_frame, placeholder_text="TestObject")
        self.entry_paneltype = customtkinter.CTkEntry(self.ui_frame, placeholder_text="PanelType")

        self.entry_rV = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rV")
        self.entry_rP = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rP")
        self.entry_ra = customtkinter.CTkEntry(self.ui_frame, placeholder_text="ra")
        self.entry_rc = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rc")
        self.entry_rf = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rf")
        self.entry_rt = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rt")
        self.entry_tc = customtkinter.CTkEntry(self.ui_frame, placeholder_text="tc")
        self.entry_reportdate = customtkinter.CTkEntry(self.ui_frame, placeholder_text="reportdate")
        self.entry_rliv = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rliv")
        self.entry_rpfv = customtkinter.CTkEntry(self.ui_frame, placeholder_text="rpfv")
        self.entry_iac = customtkinter.CTkEntry(self.ui_frame, placeholder_text="iac")
        self.entry_iat = customtkinter.CTkEntry(self.ui_frame, placeholder_text="iat")
        self.entry_ctins = customtkinter.CTkEntry(self.ui_frame, placeholder_text="ctins")
        self.entry_busbar = customtkinter.CTkEntry(self.ui_frame, placeholder_text="busbar")
        self.entry_cable = customtkinter.CTkEntry(self.ui_frame, placeholder_text="cable")
        self.button = customtkinter.CTkButton(self.ui_frame, text="Kaydet", command=self.buttoncallback)

        # Arrange UI Elements in a grid
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.entry_testno.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.entry_reportno.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.entry_typeTest.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.entry_manufacturer.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.entry_client.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        self.entry_testobject.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
        self.entry_paneltype.grid(row=7, column=0, padx=10, pady=5, sticky="ew")
        self.entry_rV.grid(row=8, column=0, padx=10, pady=5, sticky="ew")
        self.entry_rP.grid(row=9, column=0, padx=10, pady=5, sticky="ew")
        self.entry_ra.grid(row=10, column=0, padx=10, pady=5, sticky="ew")
        self.entry_rc.grid(row=11, column=0, padx=10, pady=5, sticky="ew")

        self.entry_rf.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.entry_rt.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.entry_tc.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.entry_reportdate.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.entry_rliv.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        self.entry_rpfv.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        self.entry_iac.grid(row=7, column=1, padx=10, pady=5, sticky="ew")
        self.entry_iat.grid(row=8, column=1, padx=10, pady=5, sticky="ew")
        self.entry_ctins.grid(row=9, column=1, padx=10, pady=5, sticky="ew")
        self.entry_busbar.grid(row=10,column=1, padx=10, pady=5, sticky="ew")
        self.entry_cable.grid(row=11, column=1, padx=10, pady=5, sticky="ew")

        self.button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def on_resize(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.background_id, image=self.background_photo)
        self.canvas.config(width=new_width, height=new_height)

    def buttoncallback(self):
        self.deger_atama()
        #control_json.anlamli_deger_durum_flag_yaz("1")
        self.destroy()

    def deger_atama(self):
        entity_gelen_degerler.tum_degerler_tutma.gelen_deger_tutma_ilk_sayfa(
            self.entry_testno.get(),
            self.entry_reportno.get(),
            self.entry_typeTest.get(),
            self.entry_manufacturer.get(),
            self.entry_client.get(),
            self.entry_testobject.get(),
            self.entry_paneltype.get(),
            self.entry_rV.get(),
            self.entry_rP.get(),
            self.entry_ra.get(),
            self.entry_rc.get(),
            self.entry_rf.get(),
            self.entry_rt.get(),
            self.entry_tc.get(),
            self.entry_reportdate.get(),
            self.entry_rliv.get(),
            self.entry_rpfv.get(),
            self.entry_iac.get(),
            self.entry_iat.get(),
            self.entry_ctins.get(),
            self.entry_busbar.get(),
            self.entry_cable.get()
        )
        print("deneme başarılı")
        resim_yukleme_ekrani(self)   

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)     

def resim_yukleme_ekrani(self):
    self.destroy()  # Close the current window
    self.doc.save(self.dosyaadi + '.docx')
    resim_yukleme = tkresiminput.DragDropApp(self.dosyaadi)
    resim_yukleme.mainloop()

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
