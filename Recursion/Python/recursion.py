"""
Recursive has 2 importand elements 
    - base (when it stop)
    - recursive (when it call itself) 

"""

# --------- factorial -----------
def factorial(number):
    #base case
    if number == 0:
        return 1
    #recursive case
    else:
        return number*factorial(number-1)

#derive factorial
print(f"factorial of {5} is = {factorial(5)} ") # 120

# --------------------------------
"""
    Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    It starts with 0 and 1, and the sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21...
"""
# ----------- fibonacci -----------
def fibonacci(number):
    if number<=1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)
    
#derive fibonacci
print(f"fibonacci for {10} = {fibonacci(10)}")
