#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
fruits = {
  "banana": "kela",
  "apple" : "sev",
  "grapes": "angoor",
  "pine apple": "ananas",
  "guava" : "amrood"
}
fruit = input("enter the word you want meaning of:")
print(fruits[fruit])



#Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set()
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
number = input("enter the numbers")
s.add(int(number))
print(s)



#Can we have a set with 18 (int) and '18' (str) as a value in it?
o = set()
o = {18, '18'}
print(o)
#Ans: yes, we have a set with 18 (int) and '18' (str) as a value in it.



#What will be the length of following set a:
a = set()
a.add(20)
a.add(20.0)
a.add('20') 
print(a)
print(len(a))
#Ans: the length of following set a is 2.



#s = {} ; What is the type of 'b'?
b = {}
print(type(b))
#Ans: the typr of b is dictionary.



#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
lang1 = input('enter your favourite language')
name1 = input('enter your name')
d.update({name1: lang1})
lang2 = input('enter your favourite language')
name2 = input('enter your name')
d.update({name2: lang2})
lang3 = input('enter your favourite language')
name3 = input('enter your name')
d.update({name3: lang3})
lang4 = input('enter your favourite language')
name4 = input('enter your name')
d.update({name4: lang4}) 
print(d)



#If the names of 2 friends are same; what will happen to the program in previous problem ?
#Ans: the last language(value) of the same "friends' name"(key)  entered will be updated



#. If languages of two friends are same; what will happen to the program in problem 6?
#Ans: nothing happens, just run the program like before.



#Can you change the values inside a list which is contained in set c?
c = {8, 7, 12, "Harry", [1,2]}
#Ans: I can't change the values inside a list which is contained in set c because a list is never contained in a set. the type of c is not a set.