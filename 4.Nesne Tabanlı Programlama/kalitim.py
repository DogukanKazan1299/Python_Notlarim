# class Person():
#     def __init__(this):
#         print("Person Created...")


# class Student(Person):
#     pass

# p1=Person()
# s1=Student()





# class Person():
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname
#         print("Person Created...")

# class Student(Person):
#     def __init__(self, name, surname):
#         Person.__init__(self,name,surname)
#         print("Student Created")

# p1=Person("Doğukan","Kazan")
# s1=Student("Behzat","Ç.")





# class Person():
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname
#         print("Person Created...")

#     def eating(self):
#         print("Person is eating")

#     def walking(self):
#         print("Person is walking")


# class Student(Person):
#     def __init__(self, name, surname):
#         Person.__init__(self,name, surname)
#         print("Student Created")
    
#     #Override
#     def walking(self):
#        print("Student is walking")


# p1=Person("Doğukan","Kazan")
# s1=Student("Ali","Çınar")
# p1.eating()
# s1.eating()
# p1.walking()
# s1.walking()





class Person():
    
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print("Person Created..")
    
class Student(Person):
    def __init__(self, name, surname,age):
        self.age=age
        Person.__init__(self,name,surname)
        print("Student Created...")

p1=Person("Doğukan","Kazan")
s1=Student("Doğukan","Kazan",22)
print(s1.age)