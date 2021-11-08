#Operatörler;
#atama eşit mi büyük küçük operatörleri 
x=1
y=2
z=3

print(x,y,z)

x,y,z = 5,10,15
print(x,y,z)

x=12
y=12
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#and,or,not mantıksal operatörleri işlendi 

#identity operator : is
a=b=[1,2,3]
c=[1,2,3]
print(a==b)
print(a==c)
print(a is b)
print(a is c)


#membership operatörü : in
list=["elma","muz"]
print("muz" in list)

name="Doğukan"
print("a" in name)
print("a" not in name)