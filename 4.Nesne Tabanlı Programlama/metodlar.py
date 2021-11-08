class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie Created...")
    

    def __str__(self):
        return ("Title : " + self.title + " Director: " + self.director)
    
    def __len__(self):
        return (self.duration)
    
m=Movie("Yüzüklerin Efendisi" , "Doğukan Kazan" ,120)

print(str(m))
print(len(m))


#Objeyi silme
del m