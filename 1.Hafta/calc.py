sayı1 = 134
sayı = 3453
bölme = sayı/sayı1
print("Bu bölme işleminin sonucu:" + str(bölme))

print("Bu işlem önceliğine örnek bir problem::" + (str((87+34)*12/6)))

sayı2 = 34
sayı3 = 54
çarpma = sayı2*sayı3
print("Bu çarpma işleminin sonucu:" + str(çarpma))

print("Bu işlemin sonucu:" + str((54.65+23.42)*34.12/32))

sayı6 = 34.873445
sayı7 =4653.71
t = sayı6*sayı1/sayı7
print("Bu çarpma ve bökme işleminin sonucu:" + str(t))
if t > çarpma:
    print("5.işlemin sonucu,3.işlemin sonucundan büyük")
else:
    print("5.işlemin sonucu,3.işlemin sonucundan küçük")
if çarpma > bölme:
    print("3.işlemin sonucu,1.işlemin sonucundan büyük")
else:
     print("4.işlemin sonucu,1.işlemin sonucundan küçük")

