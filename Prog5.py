
# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask user for input
num = int(input("Enter the position (n) to find the nth Fibonacci number: "))

# Call the function and print the result
print(f"The {num}th Fibonacci number is:", fibonacci(num))