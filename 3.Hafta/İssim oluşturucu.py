bitis = True
while bitis == True:
    print("----------------------------------------------------------------------------------------------------")
    print("İsim oluşturma aracına hoşgeldiniz")
    print("")
    soru =input("Devam etmek için 1,çıkmak 2 için yazın:")
    if soru == "1":
        print("")
        print("Not:Eğer vereceğiniz cevapta boşluk varsa boşluksuz yazın")
        print("")
        print("Not2:Sadece ilk sorunun baş harfini büyük yazın")
        print("")
        soru1 = input("En sevdiğiniz filmin adı:")
        print("")
        soru2 = input("En sevdiğiniz renk:")
        print("")
        soru3 = input("En sevdiğiniz hayvan:")
        x = soru1[2:]
        y = soru2[1:3]
        z = soru3[:3]
        print("Oluşturulan isim: " + x+y+z)      
        cikis1 = input("Yeniden oluşturmak için 1,Çıkmak için 2 yazın:")
        if cikis1 =="1":
            bitis = True
        elif cikis1 == "2":
            print("Çıkış yapılıyor...")
            bitis = False
    elif soru =="2":
        print("Çıkış yapılıyor")
        bitis = False