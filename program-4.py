try:
    # Ask the user for two numbers
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    # Try to divide
    result = numerator / denominator
    print("Resul:",result)

except ZeroDivisionError:
    # Handle the division by zero error
    print("Error: Cannot divide by zero!")

except ValueError:
    # Handle non-integer input
    print("Error: Please enter valid integers!")

finally:
    # This block always runs
    print("Execution completed.")
