#. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same
try:
    with open("1.txt") as f1:
        print(f1.read())
except Exception as e:
    print(e)


try:
    with open("2.txt") as f2:
        print(f2.read())      
except Exception as e:
    print(e)


try:
    with open("3.txt") as f3:
        print(f3.read())
except Exception as e:
    print(e)




#Write a program to print third, fifth and seventh element from a list using enumerate function
l = [1, "aman", 2, 5, "AK", 56, 7, 45]
for i , item in enumerate(l):
    if i == 2 or i == 4 or i == 6 :
        print(i, item)




#Write a list comprehension to print a list which contains the multiplication table of a user entered number
n = int(input("enter mumber here: "))
l = [n*i for i in range(1, 11)]
print(l)




#Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try:
    a = 5
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError as v:
    print("infinite")




# Store the multiplication tables generated in problem 3 in a file named Tables.txt
n = int(input("enter mumber here: "))
table = [n*i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(f"the table of {n}: {str(table)} \n")
