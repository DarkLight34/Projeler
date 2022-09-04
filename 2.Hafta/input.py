not1 = input("Notunuzu girin:")
if int(not1) < 0 or int(not1) > 100:
    print("Br hata oluştu")


elif int(not1) >= 90 and int(not1) <= 100:
    print("Sınav notunuz:AA (Pekiyi)")
elif int(not1) >= 85 and int(not1) <= 89:
    print("Sınav notunuz:BA (İyi-Pekiyi)")
elif int(not1) >= 80 and int(not1) <= 84:
    print("Sınav notunuz:BB (İyi)")
elif int(not1) >= 70 and int(not1) <= 79:
    print("Sınav notunuz:CB (Orta-İyi)")
elif int(not1) >= 60 and int(not1) <= 69:
    print("Sınav notunuz:CC (Orta)")
elif int(not1) >= 55 and int(not1) <= 59:
    print("Sınav notunuz:DC (Geçer-Orta)")
elif int(not1) >= 50 and int(not1) <= 54:
    print("Sınav notunuz:DD (Geçer)")
elif int(not1) >= 40 and int(not1) <= 49:
    print("Sınav notunuz:FD (Geçmez")
elif int(not1) >= 0 and int(not1) <= 39:
    print("Sınav notunuz:FF (Geçmez)")
