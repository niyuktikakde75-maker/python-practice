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




#____________Section 3:program using Multiple Objects___________
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
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary
# employees = [
#       Employee("Amit",40000),
#       Employee("Sumit",50000),
#       Employee("Ankit",55000)

#     ]   
# Highest_salary = max(employees, key=lambda employee : employee.salary)
# print("Highest Paid Employee:",Highest_salary.name) 
# print("Salary:",Highest_salary.salary)



#24
# class Books:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# books =[
#     Books("Python Basics",500),
#     Books("Advanced Python",750),
#     Books("Data Sciences",900),
#     Books("C Programming",400)
# ] 

# count = 0
# for book in books:
#     if book.price > 500:
#         count += 1
#         print(book.name,"-",book.price)
# print("Number of books above 500 =",count)        



#25
#Find the player with the heighest score.
# class player:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# players =[
#     player("Virat",95),
#     player("Rohit",120),
#     player("Rahul",80)
# ] 
# Highest_score = max(players, key = lambda Players : Players.score)
# print("Top Player:",Highest_score.name)  
# print("Highest score:",Highest_score.score)     



#26
#Compare the price of two mobile objcts.
# class Mobile:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# mobile1 = Mobile("Samsung",30000)
# mobile2 = Mobile("Onepluse",35000)

# if mobile1.price > mobile2.price:
#     print(mobile1.name ,"is more expansive")
# elif mobile2.price > mobile1.price:
#     print(mobile2.name,"is more expansive")
# else:
#     print("both mobile are of same price")
# 
# 
# 
# 27
# Transfer money between two bank account object.
# class bankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def transfer(self,receive , amount):
#         if amount <=0:
#             print("Transfer amount must be positive")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             receive.balance += amount
#             print("Money transfer successfully")

#     def display(self):
#         print(self.name,"balance:",self.balance)

# account1 = bankAccount("amit",10000)
# account2 = bankAccount("sumit",5000)

# account1.transfer(account2,3000)
# account1.display()
# account2.display()




#28
# sort student object according to marks.
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
# students = [
#     student("Amit",75),
#     student("Pooja",92),
#     student("Sneha",82),
#     student("Rahul",65)


# ]  

# students.sort(key = lambda student:student.marks,reverse=True)

# for student in students:
#     print(student.name , student.marks)



#29
# Display car costing less than 10,00,000
# class car:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# cars =[
#     car("tata Punch",700000),
#     car("hyundai",1300000),
#     car("Swift",800000),
#     car("mahindra XUV700",1800000)
# ]  
# print("car below 10,00,000:")
# for car in cars:
#     if car.price < 1000000:
#         print(car.name,"-",car.price)      




#30
#calculate the average salary of employee
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
# Employees =[
#     Employee("Amit",40000),
#     Employee("Sumit",50000),
#     Employee("Mohit",45000),
#     Employee("rahul",55000)
# ]   

# total_salary = 0
# for Employee in Employees:
#     total_salary += Employee.salary

# average_salary = total_salary / len(Employees)
# print("average Salary:",average_salary)    




#_________Section 4:Class variable,static Method and class Method________
#31
#Use a class variable for the school name.
# class student:
#     school_name ="sonu Career institute"

#     def __init__(self,name,roll_number):
#         self.name = name
#         self.roll_number = roll_number

#     def display(self):
#         print("Name:",self.name)
#         print("Roll Number:",self.roll_number)
#         print("School",student.school_name)  

# student1 = student("Amit",20)
# student2 = student("Suit",21)

# student1.display()   
# print()
# student2.display()      




#32
#count the number of Employee object created.
# class Employee:
#     employee_count =0

#     def __init__(self,name):
#         self.name = name
#         Employee.employee_count += 1

# employee1 = Employee("Amit")        
# employee2 = Employee("sumit")        
# employee3 = Employee("Rahul")  

# print("Total employee:",Employee.employee_count)


#33
#Use a Common bank name for all account object.
# class bank:
#     bank_name ="state Bank of india"

#     def __init__(self,account_holder):
#         self.account_holder = account_holder

#     def display(self):
#         print("account Holder:",self.account_holder)
#         print("Bank Name:",bank.bank_name)

# account1 = bank("Amit")
# account2 = bank("rahul")
# account1.display()
# print()
# account2.display()


#34
# Calculate a product price after a class-level discount.
# class product:
#     discount_percentage = 10

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def discounted_price(self):
#         discount = self.price * product.discount_percentage /100
#         return self.price - discount

# product1 = product("laptop",600000)

# print("Product:",product1.name)
# print("original Price:",product1.price)
# print("discounted price:",product1.discounted_price())



#35
#store a common college name for different students.
# class CollegeStudet:
#     college_name = "Tulsiramji Gaikwad Patil college of Engineering and Technology"

#     def __init__(self,name,branch):
#         self.name = name
#         self.branch = branch

#     def display(self):
#         print("Student Name:",self.name)
#         print("Branch:",self.branch)
#         print("College Name:",CollegeStudet.college_name)

# student1 = CollegeStudet("Amit","ECE")
# student2 = CollegeStudet("Sumit","Biotechnology")
# student1.display()
# print()
# student2.display()



#36
#check whether a number is even or odd using a static method.
# class MathUtility:
#     @staticmethod
#     def check_even_odd(number):
#         if number % 2 == 0:
#             return "Even"
#         return "Odd"

# print(MathUtility.check_even_odd(25))
# print(MathUtility.check_even_odd(40))   


#37
#chamge the School name using a class method.
# class Student:
#     school_name = "Old school"

#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name = new_name

#     def display(self):
#         print(self.name,"-",Student.school_name)

# Student.change_school_name("Sonu Acreer Institute")
# Student1 = Student("Amit")
# Student2 = Student("sumit")
# Student1.display() 
# print()
# Student2.display()              


#38
# Update a company name using a class methhod
# class Employee:
#     comapny_name = "ABC limited"

#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def update_company(cls,new_company):
#         cls.comapny_name = new_company

#     def display(self):
#         print("Employee:",self.name)
#         print("company",Employee.comapny_name)   

# Employee.update_company("Tech Solution Private Limited")
# Employee1 = Employee("Rahul")
# Employee1.display()      
# 
# 


#39
#perform addition and multiplication using statis method.
# class Calculator:
#     @staticmethod
#     def add(number1 , number2):
#         return number1 + number2
#     @staticmethod
#     def multiply(number1,number2):
#         return number1 * number2

# print("Addition:",Calculator.add(50,10))    
# print("Multiplication:",Calculator.multiply(50,10))   
# 
# 
# 
# 40
# convert Celsius to Fahrenheit using static mathod.
# class Tempeture:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return(celsius * 9/5) + 32 

# temperature = float(input("Enter temperature in celsius:"))
# print("temperature in fehrehneit:", Tempeture.celsius_to_fahrenheit(temperature))


#_______section 5:special Method and Operator Overloading________
#41
# Display student information using_str_()  
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def __str__(self):
#         return f"Student Name:{self.name},Marks:{self.marks}"

# student1 = student("amit",85)      
# print(student1)    

#42
# Display book information using __str__()
# class book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author 
#         self.price = price
#     def __str__(self):
#         return(f"Title:{self.title},Author:{self.author}," f"price:{self.price}")    

# book1 = book("python programming","John ",599)
# print(book1)    


#43.
#add two object using operator overloading.
# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other):
#         return Number(self.value + other.value)
#     def __str__(self):
#         return str(self.value)    

# Number1 = Number(10)
# Number2 = Number(20)
# Number3 = Number1 + Number2

# print("sum :",Number3)



#44
#Compare two Product price using the less-than operator.
# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def __lt__(self, other):
#         return self.price < other.price

# product1 = product("Mousee",500)
# product2 = product("keyboard",1000)

# if product1 < product2:
#     print(product1.name ,"is cheaper")
# else:
#     print(product2.name,"is cheaper")    


#45
#Compare the two marks of two students using the greater than operator.
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def __gt__(self, other):
#         return self.marks > other.marks

# student1 = student("amit",85)
# student2 = student("Sneha",92)

# if student1 > student2:
#     print(student1.name,"has higher marks")
# else:
#     print(student2.name,"has higher marks")    



#__________section 6:Real World Programs and Mini Projects____________

#46
#Create a simple ATM system.
# class ATM:
#     def __init__(self,account_holder,balance = 0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def check_balance(self):
#         print("Available Balance:",self.balance)  

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposite Successfully")
#         else:
#             print("Invalid deposite amount")

#     def withdrawal(self,amount):
#         if amount <= 0:
#             print("invalid withdrawal amount") 
#         elif amount > self.balance:
#             print("insufficient balance")
#         else:
#             self.balance -= amount
#             print("Withdrawal successfully")   

# atm = ATM("Amit",10000)
# atm.check_balance()
# atm.deposit(2000)
# atm.withdrawal(1000)
# atm.check_balance()        



#47
#Create a simple library system.
# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self,book_name):
#         self.books.append(book_name)
#         print(book_name,"Added Successfully")    

#     def issue_book(self,book_name):
#         if book_name in self.books:
#             self.books.remove(book_name)
#             print(book_name,"issused successfully")
#         else:
#             print("Book is not availabl")  

#     def return_book(self,book_name):
#         self.books.append(book_name)
#         print(book_name,"returned successfully")   

#     def display_books(self):
#         print("Available Books:") 
#         for book in self.books:
#             print(book)


# library = Library()
# library.add_book("Python Basics")
# library.add_book("c++ Programming")
# library.add_book("Java Programming")
# library.issue_book("Python Basics")
# library.return_book("Python Basics")
# library.display_books()


#48
#Store and display hospital patients details.
# class hostipalptient:
#     def __init__(self,name,age,disease,doctor,treatment_cost):
#         self.name = name
#         self.age = age
#         self.disease = disease
#         self.doctor = doctor
#         self.treatment_cost = treatment_cost

#     def display(self):
#         print("Ptient Name:",self.name),
#         print("Patient Age:",self.age),
#         print("Disease:",self.disease),
#         print("Doctor:",self.doctor),
#         print("Treatment Cost:",self.treatment_cost)

# patient1 = hostipalptient("Rahul",35,"Fever","Dr.Sharma",2500)
# patient1.display()    
# 
#concept:A class can represent a real-world record with related fields.


#49
#create a restaurant billing system.
# class RestaurantOrder:
#     def __init__(self):
#        self.items=[]
#     def add_item(self,name ,quantity,price):
#          self.items.append({
#             "name":name,
#             "quantity":quantity,
#             "price":price,

             
#          })
#     def calculatr_bill(self):
#         total = 0
#         for item in self.items:
#             total+=item["quantity"]*item["price"]
#         return total    

#     def display_bill(self):
#         print("Restaurant Bill") 
#         for item in self.items:
#             item_total = item["quantity"]*item["price"]
#             print(item["name"],item["quantity"],item["price"],item_total)  
#         print("Final Bill:",self.calculatr_bill())         

# order = RestaurantOrder()
# order.add_item("pizza:",2,250)
# order.add_item("Burger:",3,120)
# order.add_item("cold Drink:",2,50)
# order.display_bill()
#
#Concept:The order object stores many items and calculats the complete bill.



#50.
# Create an online course class wit student enrolment.
# class onlineCourse:
#     def __init__(self,course_name,instructor,fees,duration):
#         self.course_name= course_name
#         self.instructor = instructor
#         self.fees = fees
#         self.duration = duration
#         self.students =[]

#     def enrol_student(self,student_name):
#         self.students.append (student_name) 
#         print(student_name,"enrolled successfullly")

#     def display(self):
#         print("Course:",self.course_name)
#         print("Instructor:",self.instructor)
#         print("Fees:",self.fees)
#         print("Duration:",self.duration)
#         print("Enrolled Students:",self.students)     

# course1 = onlineCourse("pythnon Programming","Sonu sir",5000,"3 months")
# course1.enrol_student("Amit")
# course1.enrol_student("Sumit")
# course1.display()
#An object can maintain a growing list of enrolled students.


#51
#create a student management system.
class student:
    def __init__(self,roll_number,name,marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def display(self):
        print(self.roll_number,self.name,self.marks)

class studentManagement:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def search_student(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                student.display()
                return
        print("student not fonud")

    def display_all(self):
        for student in self.students:
            student.display()

management = studentManagement()
management.add_student(student(1,"amit",85))
management.add_student(student(2,"Sneha",90))
management.add_student(student(3,"Rahul",75))
management.display_all()
print("\nSearch Result:")
management.search_student(2)                 

                               

         
 
       


                    
        
