#Koşullu Durumlar

#1.
# sinavNotu=int(input("Notunuzu giriniz"))

# if sinavNotu>50:
#     print("Dersi Gectiniz")
# else:
#     print("Kaldınız")


#2.
yas=int(input("Yaşınızı Giriniz : "))
if 0<yas<10:
    print("Çocuk")
elif 10<=yas<20:
    print("Ergen")
elif 20<=yas<45:
    print("Yetişkin")
else:
    print("Yaşlı")