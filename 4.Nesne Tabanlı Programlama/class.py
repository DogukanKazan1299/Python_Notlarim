#class yazmak ve obje oluşturmak ; 

# class Person:
#     pass

# p1=Person()
# print(p1)



#Constructor Yapısı -> __init__
# class Person:
#     pass

#     def __init__(self,name,year):
#         self.name=name
#         self.year=year


# p1=Person("Doğukan",2021)
# print(p1.name)
# print(p1.year)

# p2=Person("Ali",2022)
# print(p2.year,p2.name)






class Person:
    
      #class attribute
        address="Bilgi Yok"
        gender="Erkek"

      #constructor
        def __init__(this,name,age):
            this.name=name
            this.age=age

#object->instance
person1=Person("Doğukan",22)
print(person1.name,person1.age,person1.address,person1.gender)


