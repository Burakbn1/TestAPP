import tkinter
import customtkinter
from PIL import Image, ImageTk
import deger_alma_ilk_sayfa
import kayit_dosyasi_olusturma
import control_json
import entity_gelen_degerler

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Siemens Test App")
        self.geometry(f'{1100}x{700}+{700}+{500}')

        # Tam ekran modunu etkinleştir
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.exit_fullscreen)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Siemens", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=10)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Kayıt Dosya Yolu Belirle", command=self.sidebar_button_event_ana_dosya_yolu)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Server Push Yolu Belirle", command=self.sidebar_button_event_server_dosya_yolu)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Disabled CTkButton", state="disabled")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main frame for the background image
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, columnspan=7, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
    
        self.background_image = Image.open("Siemens.jpg")

        if self.attributes('-fullscreen'):
            self.background_image = self.background_image.resize((1920, 1080), Image.LANCZOS)
        else:
            self.background_image = self.background_image.resize((1100, 700), Image.LANCZOS)

          # Resize the image to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Canvas oluştur ve arkaplan resmini yerleştir
        self.canvas = tkinter.Canvas(self.main_frame)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Dielectric Test")
        self.tabview.add("Isı Testi")
        self.tabview.add("Şebeke Frekans Testi")
        self.tabview.tab("Dielectric Test").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Isı Testi").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Dielectric Test"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        #self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Dielectric Test"),
        #                                            values=["Value 1", "Value 2", "Value Long....."])
        #self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Dielectric Test"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Isı Testi"), text="CTkLabel on Isı Testi")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="n")

        # create textbox
        self.textbox_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.textbox_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox = customtkinter.CTkEntry(self.textbox_frame, width=300, height=30, placeholder_text="Enter text here")
        self.textbox.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="ew")

        # create another tabview for reports
        self.report_tabview = customtkinter.CTkTabview(self, width=300)
        self.report_tabview.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.report_tabview.add("Dielectric Test")
        self.report_tabview.add("Isı Testi")
        self.report_tabview.add("Şebeke Frekans Testi")
        self.report_tabview.tab("Dielectric Test").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.report_tabview.tab("Isı Testi").grid_columnconfigure(0, weight=1)

        self.report_button = customtkinter.CTkButton(self.report_tabview.tab("Dielectric Test"), text="Yeni Dosya Oluştur.", command=self.test_olustur)
        self.report_button.grid(row=2, column=0, padx=20, pady=(20, 10))
        self.new_file_name = customtkinter.CTkEntry(self.report_tabview.tab("Dielectric Test"), placeholder_text="Oluşturulacak Rapor Adını girin")
        self.new_file_name.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        
        #self.report_combobox_1 = customtkinter.CTkComboBox(self.report_tabview.tab("Dielectric Test"),
        #                                                   values=["Value 1", "Value 2", "Value Long....."])
        #self.report_combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        #self.report_string_input_button = customtkinter.CTkButton(self.report_tabview.tab("Dielectric Test"), text="Open CTkInputDialog",
        #                                                          command=self.open_input_dialog_event)
        #self.report_string_input_button.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.report_label_tab_2 = customtkinter.CTkLabel(self.report_tabview.tab("Isı Testi"), text="CTkLabel on Isı Testi")
        self.report_label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=2, column=0, pady=20, padx=20, sticky="n")

        # set default values
        self.checkbox_1.select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        #self.combobox_1.set("CTkComboBox")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event_ana_dosya_yolu(self):
        dialog = customtkinter.CTkInputDialog(text="Dosya Kaydetmek İstediğiniz Yolu Giriniz:", title="DosyaKayıtYolu")
        dosya_kayit_yolu= dialog.get_input()
        control_json.deger_degistir(dosya_kayit_yolu, 1)

    def sidebar_button_event_server_dosya_yolu(self):
        dialog = customtkinter.CTkInputDialog(text="Dosya Göndermek İstediğiniz Server Yolunu Giriniz:", title="DosyaKayıtYolu")
        dosya_kayit_yolu= dialog.get_input()
        control_json.deger_degistir(dosya_kayit_yolu, 2)



    def test_olustur(self):
        
        entity_gelen_degerler.tum_degerler_tutma.test_no_alma_func(self.new_file_name.get())
        
        
        self.destroy()

        deger_alma_sayfa= deger_alma_ilk_sayfa.App()
        deger_alma_sayfa.mainloop()
        #dialog = customtkinter.CTkInputDialog(text="Test adını giriniz:", title="TestKayıtDosyasıOluştur")
        #test_adi= dialog.get_input()
        #print("Test Adı:", test_adi)
        #kayit_dosyasi_olusturma.create_save_file(test_adi)
        
        print("Yeni Test Oluşturma Başlat")
    

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)

if __name__ == "__main__":
    app = App()
    app.mainloop()
