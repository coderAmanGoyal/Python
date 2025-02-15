import random

#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’
with open("poems.txt", "r") as f:
  content = f.read()
  if("twinkle" in content):
    print("this file contains word 'twinkle'")
  else:
    print("this file doesn't contain word twinkle")




#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
def game():
  score = random.randint(1, 50)
  print(f"Your current score: {score}")

  with open("Hi-score.txt") as a:
    hiScore = a.read()
    if (hiScore != ""):
      hiScore = int(hiScore)
    else:
      hiScore = 0
    print(f"High Score: {hiScore}")    

  if(score > hiScore):
    with open("Hi-score.txt", "w") as a:
      a.write(score)

game() 




#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old
def mltTable(n):
  table = ""
  for i in range(1, 11):
    table += f"{n} X {i} = {n*i}"
  with open("tables/table_{n}.txt", "w") as f:
    f.write(table)    

for i in range(2, 21):
  mltTable(i)
  



#A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file
word = "donkey"
with open("file.txt", "r") as f:
  content = f.read()
contentNew = content.replace(word, "#"*len(word))
with open("file.txt", "w") as f:
  f.write(contentNew)





#Repeat program 4 for a list of such words to be censored.
words = ["donkey", "owl", "bad"] 
with open("file.txt", "r") as f:
  content = f.read()
for word in words:
  content = content.replace(word, "#"*len(word))
with open ("file.txt","w") as f:
  f.write(content)




#Write a program to mine a log file and find out whether it contains ‘python’  
with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")






#7. Write a program to find out the line number where python is present from ques 6.
with open("file.txt") as f:
  lines = f.readlines()
  
lineNo = 1
for line in lines:
  if("python" in lineNo):
    print(f"'YES', python word is present in line {lineNo}")
    break
  lineNo += 1
else:
  print("'NO', python word is not present in this file")  




#Write a program to make a copy of a text file “this. txt”
  with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)




#Write a program to find out whether a file is identical & matches the content of another file
with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else: 
    print("No these files are not identical")  




#Write a program to wipe out the content of a file using python
with open("this_copy.txt", "w") as f:
    f.write("")




#Write a python program to rename a file to “renamed_by_ python.txt
with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)    