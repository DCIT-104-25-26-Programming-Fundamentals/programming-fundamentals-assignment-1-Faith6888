#an upgrade of calculator 1
#for this particular one we are able to use the inutuition of defining our own functions
#in this case for instance we define the sqaure of a number (which is not necessarily a function already exisisting in python)


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n ** 2
    
main()