# LOOPS
# These are my notes on lecture 3
# doing something cyclically
# while - repeat something again and again
# for - iterate over a list of items (know explicitly tbe number of times you want it to execute)
# list - represented using []
# len - length of a list
# range - takes numbers []
# dict - dictionaries, associate one value with another {}

# a program that meows like a cat

# makiing use of the while loop
#i  = 0
#while i < 5:          # a boolean expression
 #   print("meow")     # print the statement
  #  i += 1        # now update the i value by adding one it and then start from the top again since this block makes use of a loop
  
# making use of the for loop and a list
#for _ in range(3):
 #   print("meow")

# my try at the work
#n = int(input("How many times should the cat meow? "))  
#if n >= 0:
#  print("meow\n" * n, end="")
# else:
#print("Enter a valid number")

'''def main():
  number = get_number()
  meow(number)

def meow(n):
  for _ in range(n):
    print("meow")
    
def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      return n 

main() '''

# Hogwarts program - making use of lists
'''students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
  print(i + 1, students[i]) '''
  
''' students = {
  "Hermione": "Gryffindor", 
  "Harry": "Gryffindor", 
  "Ron": "Gryffindor", 
  "Draco":"Slytherin",
  } '''

''' for student in students:
  print(student, students[student], sep=" - ") '''

''' name = input("Whose house do you want to know? ")

print(students[name]) '''

# compose a lsit of dictionaries
'''students = [
  {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
  {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"}
]

for student in students:
  print(student["name"], student["house"], student["patronous"], sep=" ,")'''
  

# a bit of Mario

'''def main():

  print_row(4)
  
def print_row(width):
  print("?" * width)

main() '''

def main():
  print_square(3)
  
def print_square(size):
  
  for i in range(size):
    print("#" * size)
    


main()