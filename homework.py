#section 1:Basic Class and Object Project
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
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):   
#         return 2 *(self.length + self.width)

# rectangle1 = Rectangle(10,5)

# print("area:",rectangle1.area())
# print("perimeter:",rectangle1.perimeter())



#8
#Calculate the area and circumferences of Circle
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumferences(self):
#         return 2 * 3.13 * self.radius * self.radius  
# circle1 = circle(7)
# print("Area:",circle1.area())     
# print("Circumferences:",circle1.circumferences())  


#9
# Create three Object of the person class
# class person:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age  
#         self.city = city
#     def display(self):
#         print(self.name,self.age,self.city) 
# person1 = person("Niyukti",20,"Nagpur")
# person2 =person("Sneha",25,"wardha")
# person3 = person("Rohit",20,"pune")   

# person1.display()
# person2.display()
# person3.display()


#10
#Create a laptop class with brand,RAM,storage and price
# class laptop:
#     def __init__(self,brand,ram,storage,price):
#         self.brand=brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price
#     def display(self):
#         print("Brand:",self.brand)
#         print("RAM:",self.ram)
#         print("storage:",self.storage)
#         print("price:",self.price)

# laptop1 = laptop("HP",16,512,65000)
# laptop1.display()



#Section 2: Intermediate Object Oriented Programming
#11
#Create a bank account with deposite and withdrawal method
class BankAccount:
    def __init__(self,account_holder,balance =0):
        self.account_holder = account_holder
        self.balance = balance
    def deposite(self , amount):
        if amount > 0:
            self.balance +=amount
            print(amount,"deposite successfully")
        else:
            print("Deposite amount must be positive")
    def withdraw(self , amount):
        if amount <=0:
            print("withdrawal must e positive")
        elif amount > self.balance:
            print("insufficinet amount")
        else:
            self.balance-=amount
            print(amount,"withdrawal successfully")    
    def display_balance(self):
        print("Account holder",self.account_holder) 
        print("Current balance",self.balance) 

account1 = BankAccount("amit",5000)
account1.deposite(1000)
account1.withdraw(2000)
account1.display_balance()


