#1
#create a class named student and create one object
# class student:
#     pass
# student1=student()
# print("student object created successfully")

#2
#create a stident class with name and age attributes
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("student name :",self.name)
#         print("student age :",self.age)
# student1 = Student ("niyukti",20)
# student1.display()    
# 

#3
# create a car class with brand,model and price
class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self .price = price     
    def display(self):
        print("Brand:", self.brand)  
        print("Model:", self.model)
        print("Price:",self.price)
car1 = Car("TATA","Nexon",900000)
car2 = Car("Hyundai","Creta",1200000)

car1.display()
print()
car2.display()