ailem = ["Babam:Serdar","Annem:Didem","Ben:Deniz","Kardeşim:Doruk","Küçük kardeşim:Demokan","Kız kardeşim:Duru"]
print("Aile üyelerinin isimleri:")
for number in ailem:
    print(number)  
ailemYas = [46,44,14,12,5,4]
total = 0

for age in ailemYas:
    total = total + age
print("Ailemin toplam yaşı:")
print(total)
kacKisi = len(ailemYas)
print("Ailemde kaç kişi var:")
print(kacKisi)
print("Ailemin ortalama yaşı:")
print(total/kacKisi)