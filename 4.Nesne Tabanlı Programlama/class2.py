# class Person:
#     address="İstanbul"

#     def __init__(this,name,age):
#         this.name=name
#         this.age=age
    
#     #method ekleme
#     def intro(this):
#         print("Hello Everyone...")
    
# p1=Person("Doğukan",22)
# p1.intro()



class Person:
    address="İstanbul"

    def __init__(this,name,age):
        this.name=name
        this.age=age
    
    def work(this):
        print(this.name + " kişisi çalışıyor")

p1=Person("Doğukan",22)
p1.work()