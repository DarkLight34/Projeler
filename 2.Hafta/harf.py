cumle = input("Sesli harflerin yerini bulmak istediğiniz cümleyi yazın:")
sesliHarfler = ["a","e","ı","i","o","ö","u","ü"]
index = 0
cumleUzunlugu = len(cumle)


for harf in cumle:

    index+=1    

    print("Karşılaştıracağımız harf:" + harf)
    print("")
    if harf in sesliHarfler:
        print("Harfimiz: " + harf + " Cümlenin " + str(index)  +  " Yerindedir")
print("Cümle tarandı")

     