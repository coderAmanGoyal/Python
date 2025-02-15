#1. Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer:
  company = "Microsoft"
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin

p = Programmer("aman", 1000000, 206001)
print(p.name, p.salary, p.pin, p.company)
      



#Write a class “Calculator” capable of finding square, cube and square root of a number
class calculator:
  def __init__(self, nu):
    square = nu*nu
    cube = nu*nu*nu
    print(f"the square of the given number is '{square}'. \nthe cube of the given line is '{cube}'. \nthe square root of the given number is ")

num = calculator(int("enter number here: "))




#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class cl:
  a = 100

ob = cl
ob.a = 0
print(ob.a)  




#Add a static method in problem 2, to greet the user with hello
class calculator:
  def __init__(self, nu):
    square = nu*nu
    cube = nu*nu*nu
    print(f"the square of the given number is '{square}'. \nthe cube of the given line is '{cube}'. \nthe square root of the given number is ")
    
  @staticmethod  
  def greet():
     print("you're most welcome")

num = calculator(int(input("enter number here: ")))
num.greet()




#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
from random import randint

class Train:
  def __init__(self, train):
     self.train = train
     
  def runningStatus(self):
    print(f"the train {self.train} is running on time")
  def booking(self, fro, to):
    print(f"Ticket is booked in train no: {self.train} from {fro} to {to}")
  def fare(self):
    print(f"the fare of the train {self.train} is {randint(225, 5000)} ")

jrn = Train(12125)
jrn.runningStatus()
jrn.booking("dwarka", "ayodhya")
jrn.fare()




#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects
class name:
  def __init__(slf,  name):
    print(name)

obj = name("harry") 