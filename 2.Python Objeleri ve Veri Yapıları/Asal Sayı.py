#Asal Sayı;

sayi=int(input("Bir sayi giriniz"))
asalMi=True

if sayi==1:
    asalMi=False
for i in range(2,sayi):

    if sayi % i == 0 :
        asalMi=False
        break
if asalMi:
    print("Sayı asaldır")
else:
    print("sayı asal değildir")    
