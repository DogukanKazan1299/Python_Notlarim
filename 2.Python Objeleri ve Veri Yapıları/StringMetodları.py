#String Methodları;

name="Dogukan"

name = name.upper()
name=name.lower()
name=name.title()#Başharfler büyütülür
name=name.capitalize()#Sadece ilk harf büyür
name=name.find("o")#index numarasını arar.
#startswith->başlıyor mu
#endswith->bitiyor mu
name=name.replace("Doğukan","Ahmet")#değiştir

print(name)