#Create a class (2-D vector) and use it to create another class representing a 3-D vector
class TwoDVector:
  def __init__(self, i, j):
    self.i = i
    self.j = j

  def show(self):
    print(f"the vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.k = k

  def show(self):  
    print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(5, 2)   
a.show() 
b = ThreeDVector(2, 5, 8)
b.show()




#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’
class Animal:
  pass

class pets(Animal):
  pass

class dog(pets):
  @staticmethod
  def bark():
    print("bow bow")

tommy = dog()
tommy.bark()




#Create a class ‘Employee’ and add salary and increment properties to it Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary
class Employee:
    salary = 250
    increment = 18
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = (salary/self.salary - 1) * 100
  
kapil = Employee()
print(kapil.salaryAfterIncrement) 
kapil.salaryAfterIncrement = 300
print(kapil.increment)




#. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
        
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)




#Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them
class vector:
    def __init__(self, x,  y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(v1, v2):
        return f"{v1.x + v2.x}i + {v1.y + v2.y}j + {v1.z + v2.z}k"
    
    def __mul__(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
    
v1 = vector(3, 6, 9)
v2 = vector(2, 4, 8)
print(v1 + v2)
print(v1*v2)




# Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem
class vector:
  def __init__(self, n1, n2, n3):
    self.n1 = n1
    self.n2 = n2
    self.n3 = n3

  def __str__(self):
    return f"{self.n1}i + {self.n2}j + {self.n3}k"
  
a = vector(3, 6, 9)
print(a)




#Override the __len__() method on vector of problem 5 to display the dimension of the vector
class vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
       return len(self.l)
    
v = vector([3, 6, 9])    
print(len(v))