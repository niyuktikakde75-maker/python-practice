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
# class Car:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self .price = price     
#     def display(self):
#         print("Brand:", self.brand)  
#         print("Model:", self.model)
#         print("Price:",self.price)
# car1 = Car("TATA","Nexon",900000)
# car2 = Car("Hyundai","Creta",1200000)

# car1.display()
# print()
# car2.display()


#4
#create an Employee class with a display method
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print("emplayee name:",self.name)   
#         print("employee salary:",self.salary)
# E1 = Employee("Amit",45000)  
# E1.display()   



# 5
#create a mobile class using a constructor
# class Mobile:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def display(self):
#         print("mobile name:",self.name) 
#         print("maobile price:",self.price)       
# mobile1 = Mobile("Samsumg",20000)
# mobile1.display()



#6
#create a Book class and take information from user
# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author= author
#         self.price = price
#     def display(self):
#         print("/n")   
#         print("title:",self.title) 
#         print("author name:",self.author)
#         print("price:",self.price)
# title =input("enter book title:")   
# author =input("enter author name:")  
# price =input("enter price name:") 

# book1 = Book(title,author,price)
# book1.display()



#7
#calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):   
        return 2 *(self.length + self.width)

rectangle1 = Rectangle(10,5)

print("area:",rectangle1.area())
print("perimeter:",rectangle1.perimeter())

        