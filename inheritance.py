
#Parent/super/base class
class Animal :
    IsMammal = True

    def speak(self):
        print("Animal is speaking")

#Child class/ Sub class / Derived class
class Cat(Animal):

    def meow(self):
        print("THe cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class donkey:
    Hastail= True

    def move(self):
        print("Donkey is walking")

a = Animal()

c = Cat()


d = donkey()