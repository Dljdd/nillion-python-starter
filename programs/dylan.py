from nada_dsl import *

def nada_main(n):
    factorial = calculate_factorial(n)
    print(f"The factorial of {n} is: {factorial}")

def calculate_factorial(n):
    """
    Calculates the factorial of a given number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    
    return factorial

nada_main(5)

