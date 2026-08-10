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
# class BankAccount:
#     def __init__(self,account_holder,balance =0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposite(self , amount):
#         if amount > 0:
#             self.balance +=amount
#             print(amount,"deposite successfully")
#         else:
#             print("Deposite amount must be positive")
#     def withdraw(self , amount):
#         if amount <=0:
#             print("withdrawal must e positive")
#         elif amount > self.balance:
#             print("insufficinet amount")
#         else:
#             self.balance-=amount
#             print(amount,"withdrawal successfully")    
#     def display_balance(self):
#         print("Account holder",self.account_holder) 
#         print("Current balance",self.balance) 

# account1 = BankAccount("amit",5000)
# account1.deposite(1000)
# account1.withdraw(2000)
# account1.display_balance()


#12
#Create a calculator using class method
# class Calculator:
#     def add(self,number1,number2):
#         return number1 + number2
#     def substract(self,number1,number2):
#         return number1 - number2
#     def multiply(self,number1,number2):
#         return number1 * number2
#     def division(self,number1,number2):
#         if number2 == 0:
#             return "Division by zero is not allowed"
#         else:
#             return number1 / number2

# calculator = Calculator()   
# print("Addition:",calculator.add(10,5)) 
# print("Substraction:",calculator.substract(10,2))
# print("Multiplication:",calculator.multiply(2,2))
# print("Division:",calculator.division(2,10))       



#13
# Calculate the Total Cost of a product.
# class product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_cost(self):
#         return self.price * self.quantity

#     def display(self):
#         print("Product name:",self.name)
#         print("Price:",self.price)
#         print("quantity:",self.quantity)  
#         print("total Cost",self.total_cost())  
# product1 = product("keyboard",900,3)
# product1.display()


#14
#Calculate total,percetage,grade of a student.
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def total(self):
#         return sum(self.marks)
#     def percentage(self):
#         return self.total()/len(self.marks) 
#     def grade(self):
#         self.percentage = self.percentage()
#         if self.percentage >= 90:
#             return "A+"
#         elif self.percentage >=75:
#             return "A"
#         elif self.percentage >=60:
#             return "B"
#         elif self.percentage >=40:
#             return "C"
#         return "fail"
#     def dispaly_result(self):
#         print("Student Name:",self.name)
#         print("Total Marks:",self.total())
#         print("percentage:",self.percentage())
#         print("Grade:",self.grade())

# student1 = Student("Niyukti",[80,90,78,88,92])  
# student1.dispaly_result() 


#15
# Convert temperature using a class.
# class Temperature:
#      def celsius_to_fahrenheit(self,celsius):
#           return (celsius * 9/5)+32
#      def fahrenheit_to_celsius(self,fahrenheit):
#           return(fahrenheit - 32)*5/9
# temperature = Temperature() 
# print("fahrenheit:",temperature.celsius_to_fahrenheit(30))
# print("Celsius:",temperature.fahrenheit_to_celsius(86))   
# 
# 
# #16
# Create a simple shopping cart
# class Shoppingcart():
#     def __init__(self) :
#         self.product=[]
#     def add_product(self,name,price):
#         self.product.append({"name":name,"price":price})
#         self.name = name
#         self.price = price  
#     def display_cart(self):
#         total = 0
#         print("\n Shopping Cart")
#         for product in self.product: 
#             print(product["name"],"-",product["price"])   
#             total += product["price"]
#         print("total Bill:",total)      

# cart =Shoppingcart()
# cart.add_product("Mouse",500)
# cart.add_product("keyboard",1000)
# cart.add_product("headphone",1500)
# cart.display_cart()



#17
# calculate the empolyee Salary with HRA and DA
# class Employee:
#     def __init__(self,name,basic_salary):
#         self.name = name 
#         self.basic_salary = basic_salary
#     def hra(self):
#         return self.basic_salary * 0.20

#     def da(self):
#         return self.basic_salary * 0.10

#     def total(self):
#         return self.basic_salary + self.hra() + self.da() 

#     def display(self):
#         print("Employee:",self.name)
#         print("Basic Salary:",self.basic_salary)
#         print("HRA:",self.hra()) 
#         print("DA:",self.da())
#         print("Total salary:",self.total()) 

# employee1 = Employee("Amit",40000)
# employee1.display()        
       


# #18
# calculate an electicity bill using consumed units.
# class ElectricityBill():
#     def __init__(self,customer_name,units):
#         self.customer_name = customer_name
#         self.units = units
#     def calculate_bill(self):
#         if self.units <= 100:
#             return self.units*2
#         elif self.units <= 200:
#             return (100 * 2)+((self.units - 100)*3)
#         return (100 * 2)+(100 * 3)+((self.units - 200)*5)
#     def display(self):
#         print("Customer Name:",self.customer_name)
#         print("Consumed Units:",self.units)
#         print("Electricity Bill:",self.calculate_bill())

# bill1 = ElectricityBill("Rohit",250)
# bill1.display()        

        



#19
# Calculate a movie ticket bill.
# class MovieTicket:
#     def __init__(self,movie_name,ticket_price,number_of_tickets):
#         self.movie_name = movie_name
#         self.ticket_price = ticket_price
#         self.number_of_ticket = number_of_tickets
#     def total_price(self):
#         return self.ticket_price * self.number_of_tickets
#     def display(self):
#         print("Movie Name:",self.movie_name)
#         print("Ticket price:",self.ticket_price)
#         print("Number of Tickets:",self.number_of_ticket)

# booking1 = MovieTicket("Avengers",250,4)
# booking1.display()            





#20
# Display time in HH:MM:SS format.
# class Time:
#     def __init__(self,hours,minutes,seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#     def display(self):
#         print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

# time1 = Time(9,5,7)
# time1.display()        




#Section 3:program using Multiple Objects
#21
#Store and display the details of five students
# class Students:
#     def __init__(self,roll_number,name,marks):
#         self.roll_number = roll_number
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print(self.roll_number,self.name,self.marks)

# Student =[
#     Students(1,"Amit",85),
#     Students(2,"Sneha",90),
#     Students(3,"Pooja",75),
#     Students(4,"sumit",88),
#     Students(5,"Rohan",80)

# ]
# for Students in Student:
#     Students.display()   
# 
# 
# 
# 22
# Find the most expensive product among multiple objects.
# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# products=[
#     Product("Mouse:",500),
#     Product("Keyboard:",1500),
#     Product("Monitor:",15000)
# ]  
# expensive_product = max(products, key=lambda product : product.price)
# print("Most Expensive Product:",expensive_product.name)
# print("Price:",expensive_product.price)


#23
#Find Employee with the highest Salary.
class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
employees = [
      Employee("Amit",40000),
      Employee("Sumit",50000),
      Employee("Ankit",55000)

    ]   
Highest_salary = max(employees, key=lambda employee : employee.salary)
print("Highest Paid Employee:",Highest_salary.name) 
print("Salary:",Highest_salary.salary)
