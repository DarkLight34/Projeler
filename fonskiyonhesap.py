def çıkar(x,y):
        toplama = x - y
        print(f"{x}-{y}={toplama}")

def topla(x,y):
        toplama = x + y
        print(f"{x}+{y}={toplama}")

def çarpma(x,y):
        toplama = x * y
        print(f"{x}*{y}={toplama}")
def bölme(x,y):
        toplama = x / y
        print(f"{x}/{y}={toplama}")

bitis = True

while bitis == True:
    sayi = input("Toplama 1,Çıkarma 2,Çarpma 3 Bölme 4:")

    if sayi == "1":
        sayi1 = int(input("1.sayıyı giriniz"))

        sayi2 = int(input("2.sayıyı giriniz"))

        topla(sayi1,sayi2)

    if sayi == "2":
        sayi1 = int(input("1.sayıyı giriniz"))

        sayi2 = int(input("2.sayıyı giriniz"))

        çıkar(sayi1,sayi2)

    if sayi == "3":
        sayi1 = int(input("1.sayıyı giriniz"))

        sayi2 = int(input("2.sayıyı giriniz"))


        çarpma(sayi1,sayi2)

    if sayi == "4":
        sayi1 = int(input("1.sayıyı giriniz"))

        sayi2 = int(input("2.sayıyı giriniz"))

        bölme(sayi1,sayi2)