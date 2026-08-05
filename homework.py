#1
#create a class named student and create one object
# class student:
#     pass
# student1=student()
# print("student object created successfully")

#2
#create a stident class with name and age attributes
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("student name :",self.name)
        print("student age :",self.age)
student1 = Student ("niyukti",20)
student1.display()           