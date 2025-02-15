#Write a program to find the greatest of four numbers entered by the user.
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
d = int(input("enter a number: "))
if(a>b and a>c and a>d):
 print(a)
elif(b>a and b>c and b>d):
 print(b) 
elif(c>a and c>b and c>d):
 print(c)
else:
 print(d)



#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
 p = int(input("enter your physics exam number here: "))
c = int(input("enter your chemistry exam number here: "))
m = int(input("enter your maths exam number here: "))
if(p>=33 and c>=33 and m>=33 and p+c+m >= 120):
  print("passed")
else:
  print('failed')



#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
  p1 = "make a lot of money"
  p2 = "buy now"
  p3 = "subscribe this"
  p4 = "click this"
  msg = input("enter msg here: ")
if((p1 in msg)  or (p2 in msg) or (p3 in msg) or (p4 in msg)):
  print('this message is a spam')
else:
  print('this message is not a spam')



#Write a program to find whether a given username contains less than 10 characters or not.
username = input("enter username: ")
if(len(username)<10):
  print('TRUE, your username contains less than 10 characters')
else:
  print('False, your username characters must be less than 10')



#Write a program which finds out whether a given name is present in a list or not.
l = ["harry", "rohit", "sohan", "george"]
name = input('enter your name here: ')
if(name in l):
  print('your name is already exist in the list' )
else:
  print('your name is wonderful')



#Write a program to calculate the grade of a student from his marks from the following scheme: 90 – 100 => Ex ; 80 – 90 => A; 70 – 80 => B; 60 – 70 =>C; 50 – 60 => D; <50 => F
  num = int(input('enter marks here: '))
if(num<= 100 and num>= 90):
  print('Excellent')
elif(num<90 and num>=80):
  print('A')
elif(num<80 and num>=70):
  print('B')
elif(num<70 and num>=60):
  print('C')
elif(num<60 and num>=50):
  print('D')
else:
  print('F')



#Write a program to find out whether a given post is talking about “Harry” or not.
  post = input('enter your post here: ')
if("harry" in post):
  print('Yes, this post is talking about "Harry"')
else:
  print('No, this post is not talking about "Harry"')