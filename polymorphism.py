
#Polymorphism is many forms a method can take or have
class rectangle:
     def draw(self):
         print("Drawing a rectangle")


class Rhombus:

    def draw(self):
        print("Drwaing a rhombus")

class parallelogram:
    def draw(self):
        print("Drawing a parallelogram")



r = rectangle()

rh = Rhombus()

p = parallelogram()