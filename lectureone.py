# These are learning notes for CS50 lecture 1 - functions and variables.
# Functions, variables, conditionals, loops, exceptions, libraries, unit tests, file i/o, regular expressions, object-oriented programming,etc
# Remember to always do the command control S to save for recompiling
# Functions - action permitting you to do something in the language. An argument is an input to a function that influences it's behavior
# Side effects are what happen when you pass an argument to a function.
# Return values - give back information collected to be used for something else.
# Variables - a container for some value inside of a computer.
# Comments are notes to yourself. Make it a habit and can be used for pseudocode.
# Strings (str), also look at docs.python.org (python's official documentation, learn to read it).
# parameters - passing values to a function.
# tecno camon 50, camon 30, and s,
# getting a sense of style or conforoming to that of a company as well.
# int
# float - anumber with a decimal point



# ask user for their name
# name = input("What's your name? ")
# say hello to user
# print("Hello, ", name) 

# name = input("What's your name? ")
# print(f"hello, {name}")

#name = input("What's your name? ").strip().title()
# remove whitespaces from str and capitalize the first letter

# split user's name into first and last name
#first, last = name.split(" ")

#print(f"Hello, {first}")


#calculator lecture

#x = float(input("What's x? "))
#y = float(input("What's y? "))

#z = round(x + y)
# this is for if I want to add commas to the numbers printed out
#print(f"{z:,}")



#Making my own functions
def hello(fish = "world"):
    print("Hello, ", fish)

hello()
name = input("What's your name? ")
hello(name)
