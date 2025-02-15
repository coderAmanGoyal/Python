#Write a program using functions to find greatest of three numbers
def grtn(a, b, c):
  if(a>b and a>c):  
    return a
  elif(b>a and b>c):
    return b
  else:
    return c
  
d = grtn(10, 4, 18)  
print(d)



#Write a python program using function to convert Celsius to Fahrenheit
def cstofhr(cs):
  f = (9/5)*cs + 32  
  return f

tmp = cstofhr(24)
print(tmp)
  


#How do you prevent a python print() function to print a new line at the end
print("a")
print("b", end="")
print("c")



#Write a recursive function to calculate the sum of first n natural numbers
def sum(n):
  if (n==0):
    return 0
  return n + sum(n-1)

s = sum(10)
print(s)



# Write a python function to print first n lines of the following pattern:
# ***
# **  - for n = 3
# *
def pattern(n):
  if (n==0):
    return
  print("*"* n)
  pattern(n-1)

pattern(3)



#Write a python function which converts inches to cms
def inchtocm(inch):
  cm = inch*2.54
  return f"{cm} cm"

len = inchtocm(8)
print(len)




def rem(l, word):
  n = []
  for item in l:
     if item != word:
        n.append(item.strip(word))
  return n

l = ["aman", "rohan", "amit", "abhishek", "ann", "an"]
print(rem(l, "an"))



##Write a python function to print multiplication table of a given number
def multiply(n):
  for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

multiply(5)