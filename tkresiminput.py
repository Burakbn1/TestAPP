import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import resiminsert
import deger_alma_ilk_sayfa

class DragDropApp(TkinterDnD.Tk):
    
    def __init__(self, dosya_adi):
        super().__init__()
        self.gelen_dosya_url_total = []
        self.gelen_resim_sayisi = 0
        self.dosya_adi = dosya_adi
        print("dosya adi:"+self.dosya_adi)
        self.title("Drag and Drop Image App")
        self.geometry("800x600")

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Drag and drop images here", width=40, height=10, bg_color='green')
        self.label.pack(padx=20, pady=20, fill="both", expand=True)

        # Register the label as a drop target
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.drop)

        self.images = []  # List to store images
        self.image_labels = []  # List to store image labels
        self.file_paths = []  # List to store file paths

        self.button = ctk.CTkButton(self.frame, text="kaydet", command=self.buttoncallback)
        self.button.pack(padx=10, pady=10, side=ctk.BOTTOM)

        # Butonu en öne getirme
        self.button.lift()

    def buttoncallback(self):
        print("Hello")
        template_file = "merhaba"  # Şablon dosyanızın yolunu buraya ekleyin
        resim_insert = resiminsert.resimInsert(self.dosya_adi, self.gelen_resim_sayisi, self.gelen_dosya_url_total)
        resim_insert.islem()
        print(self.file_paths)  # Save file paths or do something with them

    def drop(self, event):
        # Get the file paths of the dropped files
        file_paths = self.tk.splitlist(event.data)
        for file_path in file_paths:
            self.gelen_resim_sayisi += 1
            print(self.gelen_resim_sayisi)
            self.load_image(file_path)
            self.file_paths.append(file_path)  # Add file path to the list
            self.gelen_dosya_url_total.append(file_path)  # Add file path to the total list
            print(file_path)
        print(self.file_paths)  # Print all file paths

    def load_image(self, file_path):
        # Open and resize the image
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        self.images.append(image)
        
        # Clear previous image labels
        for label in self.image_labels:
            label.destroy()
        
        # Clear the list of image labels
        self.image_labels.clear()

        # Display the sorted images in the label
        self.images.sort(key=lambda img: img.filename)  # Example sort, you can customize
        for image in self.images:
            photo = ctk.CTkImage(dark_image=image, size=(300, 300))
            img_label = ctk.CTkLabel(self.frame, image=photo, text="")
            img_label.image = photo  # Keep a reference to avoid garbage collection
            img_label.pack(padx=10, pady=10, side=ctk.LEFT)
            self.image_labels.append(img_label)

        # Butonu en öne getirme (her resim yüklendiğinde)
        self.button.lift()

if __name__ == "__main__":
    dosya_adi = deger_alma_ilk_sayfa.dosyaadi
    app = DragDropApp(dosya_adi)
    app.mainloop(dosya_adi)
