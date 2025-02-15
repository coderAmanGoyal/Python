#(Q1) Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
'''first we create a virtual environment and then paasing a command (pip freeze > requirements.txt) and then make a new virtual environment and then finally passing the command (pip install -r.\requirements.txt) to make similar environment'''


#(Q2) Write a program to input name, marks and phone number of a student and format it:
print("The name of the student is {}, his marks are {} and phone number is {}".format(input("enter your name: "), input("enter your marks: "), input("enter your phone number: ")))



#(Q3) A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
table = [str(7*i) for i in range(1, 11)]
print(table)
result = "\n".join(table)
print(result)




#(Q4) Write a program to filter a list of numbers which are divisible by 5.
l = [item for item in range(1,101)]
divisible = lambda x: x%5 == 0
print(list(filter(divisible, l)))



#(Q5) Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
l = [456, 432, 223, 567, 876, 980, 456]
print(l)

def func(a, b):
    if(a > b):
        return a
    return b

print(reduce(func, l))



#(Q6) Explore the ‘Flask’ module and create a web server using Flask & Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()