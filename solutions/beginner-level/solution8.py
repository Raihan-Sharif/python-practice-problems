
def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1) 
    
# Example of usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
