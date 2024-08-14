import sys, os
import gelen_veri_entity

def deger_atama_controller_func(gelen_deger):
    gelen_veri_entity.gelen_veri_entity.testno = gelen_deger
    gelen_veri_entity.deger_yaz()

deger_atama_controller_func("merhaba")