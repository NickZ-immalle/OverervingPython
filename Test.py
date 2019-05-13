class Bomen:
    def __init__(self, typeboom, kleur, naam):
        self.typeboom = typeboom
        self.kleur = kleur
        self.naam = naam

    def soort(self):
        print("Dit is een classe soort")

class Appelboom(Bomen):
    def __init__(self, typeboom, kleur, naam, vrucht):
        super().__init__(typeboom, kleur, naam)
        self.vrucht = vrucht
               
    def specifiek(self):
        print(f'Eigenlijk ben ik een Noord-Amerikaanse appelboom {self.naam}, {self.vrucht}')
    
    def soort(self):
        print('Dit is een subclasse soort')

boom1 = Bomen("normale boom", "Licht Groen", "bart")
appelboom1 = Appelboom("appel boom", "Donker groen","gertje", "appel")

boom1.soort()
appelboom1.soort()

appelboom1.specifiek()


