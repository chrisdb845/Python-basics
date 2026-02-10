

# A class is a blueprint of the object

# An object is an instance of a class

class Employee:
    #Attru=ibute/Variables

    Name = "James"
    age = 45
    gender = "Male"
    salary = 70000.00

    #Behaviour/Functions

    def eat(self):
        print("Employee eats")

employee1 = Employee|() # Creating and object
print(employee1.Name)

employee2 = Employee()

employee3 = Employee()
