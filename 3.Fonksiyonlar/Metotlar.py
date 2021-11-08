#Metotlar;
# def merhaba():
#     print("Merhaba Fonksiyonlar")

# merhaba()
# merhaba()


# def merhaba(name):
#     print("Merhaba " + name)

# merhaba("Doğukan")



# def merhaba(name="Kullanıcı"):
#     print("Merhaba " + name)

# merhaba("Doğukan")
# merhaba("Ferdi")
# merhaba()




# def selam(name):
#     return "Selam "+ name

# mesaj = selam("Doğukan")
# print(mesaj)


# def toplama(one,two):
#     return one+two

# sonuc = toplama(10,20)
# print(sonuc)


# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))

# print(add(10,20))
# print(add(10,20,30,40))


#Params Kullanmak ;
def add(*params):
    return sum(params)

print(add(15,25))
print(add(15,25,35))
print(add(15,25,35,55,100,200,300,400))