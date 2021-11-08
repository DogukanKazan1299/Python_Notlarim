#Sayı Tahmin Oyunu;
import random

sayi=random.randint(1,100)
hak=5

while hak>0:
    hak-=1
    tahmin=int(input("tahmin : "))

    if(sayi==tahmin):
        print("Tebrikler sayıyı buldunuz...")
        break
    elif sayi>tahmin:
        print("YUKARI")
    else:
        print("AŞAĞI")
    
    if hak==0:
        print("Hakkınız kalmadı tutulan sayı = {}" ,sayi)
