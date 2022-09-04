döngü = True

import random
import time

while döngü == True:
    
    bitis = True
    sifre = ("")
    
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("Şifre oluşturma aracına hoşgeldiniz")
    print("")
    
    uzunluk = int(input("Şifreniz kaç basamaklı olsun?(maksimum:54):"))
    
    print("")
    
    isaret = ["!","_","."]
    harf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    buyukHarf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if uzunluk < 55:
      
        while bitis == True:
      
            isaretyYazi = random.choice(isaret)
            sayi = random.randint(0,9)
            harfYazi = random.choice(harf)
            buyukHarfYazi = random.choice(buyukHarf)
            sifre += isaretyYazi
      
            if len(sifre) == (uzunluk):
                bitis = False
            else:
                sifre += str(sayi)
                if len(sifre) == (uzunluk):
                    bitis = False
                else:
                    sifre += harfYazi
                    if len(sifre) == (uzunluk):
                        bitis = False
                    else:
                        sifre += buyukHarfYazi
                        if len(sifre) == (uzunluk):
                            bitis = False
                        else:
                            bitis = True
      
        print("Şifreniz: " + sifre)
        print("")
      
        cikis = input("Çıkmak için 1,yeniden şifre oluşturmak için 2'ye basın:")
      
        if cikis == "1":
            döngü = False
            print("Çıkış yapılıyor...")
            time.sleep(5)
        elif cikis == "2":
            döngü = True
    elif uzunluk > 54:
        print("Lütfen maksimum değeri geçmeyin")
        print("")
        print("Ana menüye aktarılıyorsunuz")
        time.sleep(3)
        döngü = True
b