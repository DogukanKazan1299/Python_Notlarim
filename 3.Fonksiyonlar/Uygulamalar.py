#1.Gönderilen bir kelimeyi istenilen sayıda ekranda gösteren fonksiyonu yazınız.
# def yolla(kelime,sayi):
#     print(kelime*sayi)


# yolla("Bilgisayar",3)



#2.Gönderilen sınırsız sayıda parametreyi bir listeye çevir.
# def listeyeCevir(*params):
#     liste=[]

#     for param in params:
#         liste.append(param)
#     return liste

# cevir=listeyeCevir(1,2,3,4,"a","b","c")
# print(cevir)



#3.Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if(sayi%i==0):
#                     break
#             else :
#                 print(sayi)

# sayi1=int(input("1.sayıyı giriniz"))
# sayi2=int(input("2.sayıyı giriniz"))

# asalSayilariBul(sayi1,sayi2)



#4.Kendisine gönderilen sayının tam bölenlerini bulan fonksiyonu yazınız.
def bolenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

sayilar=bolenleriBul(20)
print(sayilar)