#Write a program to print multiplication table of a given number using for loop.
num = int(input('enter the number: '))
i = num
for i in range(num , 11*num , num):
  print(i)



#Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
  if(name.startswith("S")):
    print(f"hello {name}")



#Attempt problem 1 using while loop.
num2 = int(input('enter number here: '))
j = num2
while(j < 11*num2):
  print(j)
  j += num2



#Write a program to find whether a given number is prime or not.
num3 = int(input('enter the number: '))
for i in range(2 , num3):
  if(num3%i == 0):
    print('this number is not a prime number')
    break
  else:
    print('this number is a prime number')
    break



#Write a program to find the sum of first n natural numbers using while loop.
n = int(input('enter the number: '))
i = 0
sum = 0
while(i< n+1):
  sum += i
  i += 1
print(sum)
  


#Write a program to calculate the factorial of a given number using for loop.
num4 = int(input('enter the number: ')) 
mlt = 1
for i in range(1, num4+1):
  mlt *= i
  print(mlt)




#Write a program to print the following star pattern.
#  *
# ***
#***** for n = 3
n = int(input("enter the number here: "))
for i in range(1, n+1):
  print(" "*(n-i), end="")
  print("*"*(2*i-1), end="")
  print("")



#Write a program to print the following star pattern:
# *
# **
# *** for n = 3
n = int(input("enter the number here: "))
for i in range(1, n+1):
  print("*"*(i), end="")
  print("")



#Write a program to print the following star pattern.
# * * *
# *   *     for n = 3
# * * * 
n = int(input("enter the number here: "))
for i in range(1, n+1):
  if(i==1 or i==n):
    print("*"*n, end="")
    print("")
  else:
    print("*", end="")
    print(" "*(n-2), end="")
    print("*", end="")
    print("")



#Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("enter the number here: "))
for i in range(10):
  i = 10 - i
  print(f"{n} X {i} = {n*i}") 