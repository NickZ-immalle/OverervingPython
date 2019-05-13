class Parrot: 
    species = "vogel" 
    vogelteller = 0 

    def __init__(self, name, age): 
        Parrot.vogelteller += 1 
        self.name = name 
        self.age = age  

blu = Parrot("Blu", 10) 
woo = Parrot("Woo", 15) 
print(woo.name)
print(woo.vogelteller)