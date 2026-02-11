class Dog:

    def __init__(self, name, breed,hasfur):
        self.name  = name
        self.breed = breed
        self.hasfur = hasfur


    def bark(self):
        print("Woof!! Woof!!")

    def locomotive(self):
        print("walking")


dog1 = Dog("JJ", "Bulldog", True)

print(dog1.name,dog1.breed ,dog1.hasfur)
dog1.locomotive()

dog2 = Dog("Tony", "German Shepherd", True)
print(dog2.name,dog2.breed ,dog2.hasfur)



dog3  = Dog("Ann", "Siberian Husky", True)
print(dog3.name,dog3.breed ,dog3.hasfur)


