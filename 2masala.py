# 2-----------
class Kompyuter:
    def __init__(self,nomi,ram,narxi,protsessor):
        self.nomi=nomi
        self.ram=ram
        self.narxi=narxi
        self.protsessor=protsessor
    def kiritish(self):
        print(self.nomi, self.ram, self.narxi, self.protsessor)
    def chiqarish(self):
        if 4 < self.ram < 16:
            print("Kompyuter:", self.nomi)
            print("RAM:", self.ram)
            print("Narxi:", self.narxi)
            print("Protsessor:", self.protsessor)
k1=Kompyuter("HP", 8, 5000000, "Intel i5")
k2=Kompyuter("Lenovo", 4, 4000000, "Intel i3")
k3=Kompyuter("Asus", 12, 7000000, "Intel i7")
k4=Kompyuter("Acer", 16, 6000000, "Intel i5")
kompyuterlar=[k1,k2,k3,k4]
for i in kompyuterlar:
    i.kiritish()
    i.chiqarish()