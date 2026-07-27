# just by writing out comments first sort of as guidelines for the
# problem or code to be addressed you help solve the problem as well
# this is to remove any leading or trailing whitespace from the input and also to capalize the first letter of each word in the name


name = input ("What's your name? ").strip().title()

# split users name into first name and last name and then print out a greeting to the user using their first name only
first, last = name.split(" ")

print(f"Hello, {first} ")
