
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True
    
# Example of usage
number = 29
result = is_prime(number)
print(f"Is {number} a prime number? {result}")