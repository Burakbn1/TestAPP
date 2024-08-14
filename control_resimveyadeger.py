import tkinter
import customtkinter
from PIL import Image, ImageTk
import deger_alma_ilk_sayfa
import kayit_dosyasi_olusturma
import control_json
import entity_gelen_degerler
import control_resimveyadegeraraekran

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

class App(customtkinter.CTk):
        
    def __init__(self):

        super().__init__()

        self.dummy_sayi=0
        self.deger_alma_array=[]

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
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
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
        self.tabview.grid(row=2, column=1, padx= 10, pady=10, sticky="nsew")

        self.label_tab = customtkinter.CTkLabel(self.tabview, text="Değer Giriş Ekranı")
        self.label_tab.grid(row=0, column=0, sticky="nsew")

        # Seçili seçenekleri saklamak için bir sözlük oluştur
        self.selected_options = {}

        # Radyo buton gruplarını oluştur
        create_radio_button_group(self, self.tabview, "Şalter", ["Resim yükle", "Manuel giriş"], row=1, column=1)
        create_radio_button_group(self, self.tabview, "Trafo", ["Resim yükle", "Manuel giriş"], row=1, column=2)
        create_radio_button_group(self, self.tabview, "Pano", ["Resim yükle", "Manuel giriş"], row=1, column=3)

        self.devamButton = customtkinter.CTkButton(self.tabview, text="İlerle", command=self.devam_komut)
        self.devamButton.grid(row=4, column=0, padx=10, pady=10)
        
        # create textbox
        self.textbox_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.textbox_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.uyariLabel = customtkinter.CTkLabel(self.textbox_frame, text="Bu alanda değerleri resim yükleyerek görüntü işleme çekebilir veya manuel olarak girebilirsiniz. Tercih ettiğiniz işleme göre alt bölümden seçim yapabilirsiniz." + "\n" + "Yazının devamı")
        self.uyariLabel.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="ew")
        
    def dummy_action(self):
        pass  # No action performed
        
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
        dosya_kayit_yolu = dialog.get_input()
        control_json.deger_degistir(dosya_kayit_yolu, 1)

    def sidebar_button_event_server_dosya_yolu(self):
        dialog = customtkinter.CTkInputDialog(text="Dosya Göndermek İstediğiniz Server Yolunu Giriniz:", title="DosyaKayıtYolu")
        dosya_kayit_yolu = dialog.get_input()
        control_json.deger_degistir(dosya_kayit_yolu, 2)

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)
    
    def devam_komut(self):
        
        for title, var in self.selected_options.items():

            deneme_alinan_deger= "Manuel giriş"
            deneme_alinan_deger2= "Resim yükle"
           
            if (deneme_alinan_deger== var.get()):

                self.deger_alma_array.append(0)
                print(self.deger_alma_array)  
                print("Manuel giriş geldi")

            elif (deneme_alinan_deger2== var.get()):
                self.deger_alma_array.append(1)
                print(self.deger_alma_array)                
                print("Resim yükle geldi")
                
            #print(f"{title}: {var.get()}")
        control_resimveyadegeraraekran.control_resimveyadegeraraekran.control_araekran(self.deger_alma_array)

def create_radio_button_group(app, parent, title, options, row, column):
    # Seçili seçenekleri saklamak için bir StringVar kullan
    selected_option = customtkinter.StringVar(value=options[0])

    # Sözlükte bu grup için seçili değeri sakla
    app.selected_options[title] = selected_option

    # create a label for the group
    label = customtkinter.CTkLabel(parent, text=title)
    label.grid(row=row, column=column, padx=10, pady=10)

    # create radio buttons for the group
    for index, option in enumerate(options):
        radio_button = customtkinter.CTkRadioButton(parent, text=option, variable=selected_option, value=option)
        radio_button.grid(row=row + 1 + index, column=column, padx=10, pady=5, sticky="w")

if __name__ == "__main__":
    app = App()
    app.mainloop()
