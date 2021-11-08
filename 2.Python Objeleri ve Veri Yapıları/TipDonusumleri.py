x=input("1.sayiyi giriniz")
y=input("2.sayiyi giriniz")

print(type(x))#string
print(type(y))

toplam=int(x) + int(y)#string -> int 
print(toplam)


#ÖRNEK ; Yarıçapı verilen bir dairenin alanı ve çevresi? 
#Alan = pi*r*r
#Çevre = 2*pi*r
pi=3.14
r=input("Yarıçap değerini giriniz")
print(type(r))
alan=print(float(r) * float(r) * pi)
cevre=print(2 * pi * float(r))
