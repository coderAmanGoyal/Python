#Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name")
print(f"Good Afternoon {name}")


#Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
  You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Aman").replace("<|Date|>","18/10/24"))



#Write a program to detect double space in a string
a = "My name  is Aman"
print(a)
print(a.find("  "))



#Replace the double space from problem 3 with single spaces.
print(a.replace("  "," "))



#Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n \t this python course is nice.\n Thanks!"
print(letter)