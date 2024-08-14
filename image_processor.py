import cv2
import easyocr
import matplotlib.pyplot as plt

# Resim yolunu belirtin
image_path = r'C:\Users\z004ytzh\Desktop\Projeler\totalproject\a_circuit_breaker2.jpeg'
threshold = 0.25

# Resmi okuyun
img = cv2.imread(image_path)

# EasyOCR okuyucusunu oluşturun
reader = easyocr.Reader(['en'], gpu=False)

# Resimden metinleri okuyun
text_ = reader.readtext(img)

# Okunan metinleri saklamak için bir liste oluşturun
extracted_texts = []

# Okunan her bir metni işle
for t in text_:
    bbox, text, score = t
    if score > threshold:
        # Okunan metni listeye ekleyin
        extracted_texts.append((bbox, text, score))
        
        # Metni ve dikdörtgeni resim üzerine çizin
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 2)
        cv2.putText(img, text, (bbox[0][0], bbox[0][1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# Belirli bir metinden sonraki metni bulma
target_texts = ["Typ", "Ir", "Ur"]
found_targets = {text: False for text in target_texts}

matched_texts = []

i=0


for idx, (bbox, text, score) in enumerate(extracted_texts):
    print(f"Metin {idx+1}: {text} (Güven Skoru: {score})")
    
    

    for target_text in target_texts:
        if found_targets[target_text]:
            
            print(f"Metin {idx+1} (Sonraki - {target_text}): {text} (Güven Skoru: {score})")
            matched_texts.append((bbox, text,score))
            deger_tut= [text for text in matched_texts]
            tutulan_deger=[]
            #tutulan_deger= target_texts[idx]
            print(matched_texts[i][1])
            

           #print("deger_tut: "+ str(matched_texts[1]))
            i += 1
            found_targets[target_text] = False  # Tek seferlik almak için
    
    if text.strip() in target_texts:
        found_targets[text.strip()] = True

i=0

# Resmi görüntüleyin
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.axis('off')
#plt.show()
