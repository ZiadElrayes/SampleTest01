## Question 1 (The Circle Class)
"""

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self) :
        return 3.14 * (self.radius ** 2)

objectt = Circle(8)

print("The Area of the circle : ",objectt.area())

"""

## Question 2  (The Rectangle Class)
"""
class Rectangle:

    def __init__(self,Length,Width):
        self.Length = Length
        self.Width  = Width

    def area(self):
        return self.Length*self.Width 

    def perm(self):
        return self.Length + self.Width    

len = int(input("Enter the length"))
wid = int(input("Enter the Width"))    

ans = Rectangle(len,wid)

print("Area of the Rectangle : " , ans.area())
print("perimeter of the Rectangle : " , ans.perm())



"""

## Question 3 (The Employee Class)

"""
class Employee:

    def __init__(self,ID , Fname , Lname ,Salary):
        self.ID = ID
        self.Fname = Fname
        self.Lname = Lname
        self.Salary = Salary

    def  AnnualSalary(self):
        return self.Salary * 12 

    def RaiseSalary(self):
        return self.Salary * 0.15

    def EveryData(self):
        return {'ID':self.ID , 'First Name':self.Fname,'Last Name':self.Lname , 'Salary':self.Salary}


id = int(input("Enter the ID of the Employee : "))
FN = input("Enter the First name : ")
LN = input("Enter the last name :")
Sal = int(input("Enter the salary :"))                


Empo = Employee(id,FN,LN,Sal)

print("The Employees annual salary :" , Empo.AnnualSalary())
print("The Raised salary : " , Empo.RaiseSalary())
print("Employee Data : " , Empo.EveryData())

"""

## Question 4 (The Account Class)




class Account:

    def __init__(self, ID , Name , Balance):
        self.ID = ID
        self.Name = Name
        self.Balance = Balance

    def Credit(self):
        return self.Balance + amount

    def debit(self):
        if  amount <= self.Balance:
            self.Balance - amount
        else:
            print("Amount exceeded balance")
            return self.Balance

    def Transferto(self):
        if amount <= self.Balance:
             print("Transfered amount to the given account")

        else:
            print("Amount exceeded balance")
            return self.Balance 

    def Dataa(self):
        return {'ID':self.ID , 'Name': self.Name ,'Balance':self.Balance}


amount = int(input("Enter the amount :"))
Id = int(input("Enter the ID :"))
Nam = input("Enter the name :")
Bala = float(input("Enter the balance"))

ans = Account(Id, Nam , Bala)

print("The Credit :" ,ans.Credit())
print("debit",ans.debit())
print("Data :" , ans.Dataa())
