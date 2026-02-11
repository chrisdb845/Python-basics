class Student:

    def __init__(self, fullname,age,course,feespaid):
        self.fullname = fullname
        self.age = age
        self.course = course
        self.feespaid = feespaid

    def Hardworking(self):
        print("Gets good grades")

    def Playful(self):
        print("Good at sports")

print()

student1 = Student("Jane Gathonim" ,  17, "Medicine", 2000)
print(student1.fullname,student1.age,student1.course,student1.feespaid)

student1.Hardworking()

print()


student2 = Student("Mary", 20, "MIT", 3000)
print(student2.fullname,student2.age,student2.course,student2.feespaid)

print()

student3 = Student("Shon", 17, "Data Science", 5000)
print(student3.fullname,student3.age,student3.course,student3.feespaid)