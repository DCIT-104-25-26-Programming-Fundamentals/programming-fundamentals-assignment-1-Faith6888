# CONDITIONALS
# notes on lecture two of CS50 Python
# comparison of values
# a boolean expression is one that can either hold true or false as an answer.
# elif - so as soon as I get a true answer for one boolean expression, I will stop asking the other questions
# which if fails to do in that even after we have determined that a certain boolean expression is true or false we still keep asking the others.
# or, and 
# match 

#if x < y:
 #   print ("x is less than y")
    
#elif x > y:
 #   print("x is greater than to y")

#else:
 #   print("x is equal to y")

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x == y:
 #   print("x is eqaul to y")
#else:
 #   print("x is not eqaul to y")
 
 # making code that determines the grade a student should get based on their score
 

#score = int(input("What's your score? "))

#if score >= 90 and score <= 100:
 #   print("A")
#elif score >= 80 and score < 90:
 #   print("B")
#elif score >= 70 and score < 90:
 #   print("C")
#elif score >= 60 and score < 70:
 #   print("D")
#else:
 #   print("F") 


# checking parity - whether even or odd (making use of the modulo operator)
 
# we have defined a function that tells whether a number is even or odd depending on the user input   

#def main():
 #   x = int(input("What's x? "))
  #  if is_even(x):
   #     print("Even")
    #else:
     #   print("Odd")

# here we have defined a function that tells if the number is even or odd        
#def is_even(n):
 #   return n % 2 == 0
    
# main()


# new python program called house
# checking which house you are in based on name
# making use of "match"

#name = input("What's your name? ")

#match name:
 #   case "Harry" | "Hermione" | "Ron":
  #      print("Gryffindor")
   # case "Draco":
    #    print("Slytherin")
    #case _:
     #   print("Who? ")
     
# TA
# recommending a game to a user based on the difficulty they prefer and preferred number of players
# conditionals and boolean expressions

def main():
    difficulty = input("Difficult or Casual? ")
    if difficulty != "Difficult" and difficulty != "Casual":
        print("Enter a valid difficulty ")
        return

    players = input("Multiplayer or Single-player? ")
    if players != "Multiplayer" and players != "Single-player":
        print("Enter a valid number of players ")
        return
       
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend ("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend ("Klondike")
    elif difficulty == "Casual" and players == "Multi-player":
        recommend("Hearts")
    else:
        recommend ("Clock")
        
def recommend(game):
    print("You might like", game)
    
main()