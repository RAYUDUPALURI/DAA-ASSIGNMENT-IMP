def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
number = int(input("Enter a non-negative integer to compute its factorial: "))
result = factorial_iterative(number)
print(f"The factorial of {number} is: {result}")
