import json

def deger_degistir(yeni_yol, istek_flag):
    with open("dosya_yollari.json", "r") as f:      # read the json file
        variables = json.load(f)

    if istek_flag==1:
        myvar = variables["ana_dosya_yolu"]
        variables["ana_dosya_yolu"] = str(yeni_yol)

    elif istek_flag==2:
        myvar = variables["server_dosya_yolu"]    # To get the value currently stored

        variables["server_dosya_yolu"] = str(yeni_yol)    # change the variable in python
    
    with open("dosya_yollari.json", "w") as f:      # write back to the json file
        json.dump(variables, f)
    
def deger_oku():
    with open("dosya_yollari.json", "r") as f:      # read the json file
        variables = json.load(f)
   
    return variables["ana_dosya_yolu"]

def anlamli_deger_durum_flag_oku():
    with open("dosya_yollari.json", "r") as f:      # read the json file
        variables = json.load(f)
   
    return variables["anlamli_deger_durum_flag"]

def anlamli_deger_durum_flag_yaz(gelen_deger):

    with open("dosya_yollari.json", "r") as f:      # read the json file
        variables = json.load(f)

        myvar = variables["anlamli_durum_deger_flag"]
        variables["anlamli_durum_deger_flag"] = str(gelen_deger)

        variables["server_dosya_yolu"] = str(gelen_deger)    # change the variable in python
    
    with open("dosya_yollari.json", "w") as f:      # write back to the json file
        json.dump(variables, f)
