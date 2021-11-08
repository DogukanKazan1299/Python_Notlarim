#Döngüler
#1.For;
# sayilar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for x in sayilar:
#     print(x)


# isimler=["Doğukan","Ferdi","Elif","Ayça"]
# for x in isimler:
#     print(x)

# sayilar=[1,3,5,7,9,12,19,21]
# toplam=0
# for x in sayilar:
#     if(x%3==0):
#         print("3 ün katı olan sayılar = " , x)
# for y in sayilar:
#     toplam += y
#     print("Sayıların toplamı=" ,toplam)
# for z in sayilar:
#     if(z%2==1):
#         print("Sayının karesi = " ,z*z)


# sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
# for x in sehirler:
#     if x.len()==5:
#         print(x)


#2.While;
# sayi=1
# while sayi<10:
#     print(sayi)
#     sayi=sayi+1


# sayi=0
# while sayi<100:
#     if sayi%2==1:
#         print("Sayi tektir = " ,sayi)
#     else:
#         print("Sayi cifttir = " ,sayi)
#     sayi+=1        


# sayilar=[1,3,5,7,9,12,19,21]
# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i+=1

# kisiler=["Doğukan","Asya","İstanbul","Meral","Okan"]
# i=0
# while i<len(kisiler):
#     print(kisiler[i])
#     i+=1


#3.Break - Continue İfadeleri ; Break Döngüyü durdurur.Continue ise atlayıp devam eder.

# name="Doğukan Kazan"
# for x in name:
#     if x=="ğ":
#         break
#     print(x)#D ve o yu basar break gördüğünde bitirir.

# name="Doğukan Kazan"
# for x in name:
#     if x=="ğ":
#         continue
#     print(x) #Doukan Kazan yazar -> ğ yi es geçer ve devam eder.


#4.Range->Liste oluşturmamızı sağlar ;
# list=range(10)
# for x in list:-->0,1,2,...9
#     print(x)
# list=range(7,10)
# for x in list:#7,8,9
#     print(x)
# list=range(20,50,5)-->ARTIŞ MİKTARI DA VEREBİLİRİZ...
# for x in list:
#     print(x)



# #5.zip->liste birleştirebiliriz...
# list1=["Doğukan","Fernando","Burak","Ayhan"]
# list2=["Kazan","Muslera","Yılmaz","Akman"]
# print(list(zip(list1,list2)))