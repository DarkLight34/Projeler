ogrenciler = ["Duru","Deniz","Efe"]



for x in ogrenciler:
    print(x)

    not1 = input("1.Sınav notunu giriniz:")
    if int(not1) > 100 and int(not1) < 0:
        while int(not1) >=0 and int(not1) <= 100:
            print("Lütfen 0-100 arasında bir değer giriniz")
            not1 = input("1.Sınav notunu giriniz:")
    
    not2 = input("2.Sınav notunu giriniz:")
    not3 = input("3.Sınav notunu giriniz:")
    not4 = input("4.Sınav notunu giriniz:")
    toplam = int(not1) + int(not2) + int(not3) + int(not4)
    ortalama = toplam/4
    if int(not1) < 0 or int(not1) > 100 or int(not2) < 0 or int(not2) > 100 or int(not3) < 0 or int(not3) > 100 or int(not4) < 0 or int(not4) > 100:
        print("Bir hata oluştu")

    elif ortalama >= 90 and ortalama <= 100:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:AA (Pekiyi)")
    elif ortalama >= 85 and ortalama <= 89:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:BA (İyi-Pekiyi)")
    elif ortalama >= 80 and ortalama <= 84:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:BB (İyi)")
    elif ortalama >= 70 and ortalama <= 79:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:CB (Orta-İyi)")
    elif ortalama >= 60 and ortalama <= 69:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:CC (Orta)")  
    elif ortalama >= 55 and ortalama <= 59:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:DC (Geçer-Orta)")
    elif ortalama >= 50 and ortalama <= 54:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:DD (Geçer)")
    elif ortalama >= 40 and ortalama <= 49:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:FD (Geçmez)")
    elif ortalama >= 0 and ortalama <= 39:
        print(x + " öğrencisinin ortalaması:" + str(ortalama) + ",öğrencinin aldığı not:FF (Geçmez)")

