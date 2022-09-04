cumle = "bugün çok çok sıcak"

cumleBuyuk = cumle.capitalize()
print("capitalize sorsunun cevabı " + str(cumleBuyuk))

cumleBuyukHarf = cumle.title()
print("title sorusunun cevabo "  + str(cumleBuyukHarf))

cumleNumerikMi = cumle.isnumeric()
print("numerik mi sorsunun cevabı " + str(cumleNumerikMi))


x = cumle.count("çok")
print("çok kelimesi bu cümlede " + str(x) + " defa geçiyor" )
print("")
print("")

meyve = ["üzüm","elma","karpuz"]
print(meyve)

meyve.append("portakal")
meyve.append("mandalina")
print(meyve)

meyve.sort()
print(meyve)

meyve.remove("üzüm")
print(meyve)

meyve.pop()
print(meyve)
