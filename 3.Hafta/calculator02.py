bitis = True
g = True
while bitis == True:
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Hesap makinesine hoşgeldiniz")
    print("")
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Çıkış")
    yazi = input("Yapmak istediğiniz işlemi başındaki sayıyı yazarak yapabilirsiniz:")
    if yazi == "1":
        sayı1 = (input("Birinci sayıyı giriniz:"))
        t = sayı1.isnumeric()
        print("")
        sayı2 = (input("İkinci sayıyıyı girin:"))
        print("")
        y = sayı2.isnumeric()

        if t == True and y == True:
                x = (int(sayı1)+int(sayı2))
                print("Toplama işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                 bitis = False
                print("Çıkış yapılıyor...")
        elif t == False and y == False:
            while t == False and y == False:
                print("Lütfen sayı giriniz")
                sayı1 = (input("Birinci sayıyı giriniz:"))
                print("")
                sayı2 = (input("İkinci sayıyı giriniz:"))
                print("")
                t == sayı1.isnumeric()
                y = sayı2.isnumeric()
                if t == True and y == True:
                    break
            if yazi == "1":
                x = (int(sayı1)+int(sayı2))
                print("Toplama işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif t == False:
            while t == False:
                print("Lütfen Sayı girin")
                sayı1 = input("Birinci sayıyı giriniz:")
                print("")
                t = sayı1.isnumeric()
                if t == True:
                    break
            if yazi == "1":
                x = (int(sayı1)+int(sayı2))
                print("Toplama işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif y == False:
            while y == False:
                print("Lütfen Sayı girin")
                sayı2 = input("İkinci sayıyı giriniz:")
                print("")
                y = sayı2.isnumeric()
                if y == True:
                    break
            if yazi == "1":
                x = (int(sayı1)+int(sayı2))
                print("Toplama işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
    if yazi == "2":
        sayı1 = (input("Birinci sayıyı giriniz:"))
        t = sayı1.isnumeric()
        print("")
        sayı2 = (input("İkinci sayıyıyı girin:"))
        print("")
        y = sayı2.isnumeric()

        if t == True and y == True:
                x = (int(sayı1)-int(sayı2))
                print("Çıkarma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                 bitis = False
                print("Çıkış yapılıyor...")
        elif t == False and y == False:
            while t == False and y == False:
                print("Lütfen sayı giriniz")
                sayı1 = (input("Birinci sayıyı giriniz:"))
                print("")
                sayı2 = (input("İkinci sayıyı giriniz:"))
                print("")
                t == sayı1.isnumeric()
                y = sayı2.isnumeric()
                if t == True and y == True:
                    break
            if yazi == "2":
                x = (int(sayı1)-int(sayı2))
                print("Çıkarna işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif t == False:
            while t == False:
                print("Lütfen Sayı girin")
                sayı1 = input("Birinci sayıyı giriniz:")
                print("")
                t = sayı1.isnumeric()
                if t == True:
                    break
            if yazi == "2":
                x = (int(sayı1)-int(sayı2))
                print("Çıkarma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif y == False:
            while y == False:
                print("Lütfen Sayı girin")
                sayı2 = input("İkinci sayıyı giriniz:")
                print("")
                y = sayı2.isnumeric()
                if y == True:
                    break
            if yazi == "2":
                x = (int(sayı1)-int(sayı2))
                print("Çıkarma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
    if yazi == "3":
        sayı1 = (input("Birinci sayıyı giriniz:"))
        t = sayı1.isnumeric()
        print("")
        sayı2 = (input("İkinci sayıyıyı girin:"))
        print("")
        y = sayı2.isnumeric()

        if t == True and y == True:
                x = (int(sayı1)*int(sayı2))
                print("Çarpma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                 bitis = False
                print("Çıkış yapılıyor...")
        elif t == False and y == False:
            while t == False and y == False and g == True:
                print("Lütfen sayı giriniz")
                sayı1 = (input("Birinci sayıyı giriniz:"))
                print("")
                sayı2 = (input("İkinci sayıyı giriniz:"))
                print("")
                t = sayı1.isnumeric()
                y = sayı2.isnumeric()
                if t == True and y == True :
                    break
            if yazi == "3":
                x = (int(sayı1)*int(sayı2))
                print("Çarpma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif t == False:
            while t == False:
                print("Lütfen Sayı girin")
                sayı1 = input("Birinci sayıyı giriniz:")
                print("")
                t = sayı1.isnumeric()
                if t == True:
                    break
            if yazi == "3":
                x = (int(sayı1)*int(sayı2))
                print("Çarpma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif y == False:
            while y == False:
                print("Lütfen Sayı girin")
                sayı2 = input("İkinci sayıyı giriniz:")
                print("")
                y = sayı2.isnumeric()
                if y == True:
                    break
            if yazi == "3":
                x = (int(sayı1)*int(sayı2))
                print("Çarpma işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")                   
    if yazi == "4":
        sayı1 = (input("Birinci sayıyı giriniz:"))
        t = sayı1.isnumeric()
        print("")
        sayı2 = (input("İkinci sayıyıyı girin:"))
        print("")
        y = sayı2.isnumeric()

        if t == True and y == True:
                x = (int(sayı1)/int(sayı2))
                print("Bölme işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                 bitis = False
                print("Çıkış yapılıyor...")
        elif t == False and y == False:
            while t == False and y == False and g == True:
                print("Lütfen sayı giriniz")
                sayı1 = (input("Birinci sayıyı giriniz:"))
                print("")
                sayı2 = (input("İkinci sayıyı giriniz:"))
                print("")
                t = sayı1.isnumeric()
                y = sayı2.isnumeric()
                if t == True and y == True :
                    break
            if yazi == "4":
                x = (int(sayı1)/int(sayı2))
                print("Bölme işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif t == False:
            while t == False:
                print("Lütfen Sayı girin")
                sayı1 = input("Birinci sayıyı giriniz:")
                print("")
                t = sayı1.isnumeric()
                if t == True:
                    break
            if yazi == "4":
                x = (int(sayı1)/int(sayı2))
                print("Bölme işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")
        elif y == False:
            while y == False:
                print("Lütfen Sayı girin")
                sayı2 = input("İkinci sayıyı giriniz:")
                print("")
                y = sayı2.isnumeric()
                if y == True:
                    break
            if yazi == "4":
                x = (int(sayı1)/int(sayı2))
                print("Bölme işleminin sonucu:" + str(x))
                print("")
                geriDonus = input("Yeniden işlem yapmak için 1,çıkmak için 2 yazınız:")
                if geriDonus == "1":
                    bitis = True
                elif geriDonus == "2":
                    bitis = False
                    print("Çıkış yapılıyor...")              
    elif yazi == "5":
        print("Çıkış yapılıyor...") 
        bitis = False