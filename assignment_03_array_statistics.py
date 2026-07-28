# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

# defining a function that finds the sum of a set of numbers
def calc_sum(numbers):
    total = 0 
    for num in numbers:
        total = total + num  # cumulative total
    return total # return the final value


# defining a function that finds the average of a set of numbers
def calc_average(numbers):
    total = calc_sum(numbers)
    count = len(numbers)  # this gives us the number of numbers the user has requested to input
    return total / count

# defining a function that finds the max number among several numbers
def calc_maximum(numbers):
    highest = numbers[0]  
    for num in numbers:
        if num > highest:
            highest = num  # Update champion if we find a larger number
    return highest

def calc_minimum(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest 

def main():
    n = int(input("How many numbers would you like to enter? "))

    if n <= 0:
        print("Error: Please enter a positive integer (a number greater than 0).")
        return 
    
    numbers = []  # Empty list memory to store user entries
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)
        
    print("\nResults:")
    print(f"The sum is: {calc_sum(numbers)}")
    print(f"The average is: {calc_average(numbers)}")
    print(f"The maximum number is: {calc_maximum(numbers)}")
    print(f"the minimum number is: {calc_minimum(numbers)}")
        
# Run the main program
if __name__ == "__main__":
    main()
