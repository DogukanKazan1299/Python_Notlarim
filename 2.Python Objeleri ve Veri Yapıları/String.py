name="Doğukan"
surname="Kazan"
age=22

#int to string -> by str
hi="Hello My name is " + name + " Surname is " + surname + "\nI am " + str(age) +" years old."
print(hi)

print(name[2])


x="Doğukan Kazan"
y="Bilgisayar Mühendisi"
z=22
print("Merhabalar,\nAdım {} {} olarak çalışmaktayım\nYaşım ise {}'dir" .format(x,y,z))