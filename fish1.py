#creating my own function

def hello(to="world"):
    print("Hello, ", to)
    
hello()
name = input("What's your name? ").strip().title()
hello(name)
