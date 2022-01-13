# Write a program to create a recursive function to calculate the factorial of number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
res = factorial(int(input('enter number:')))
print('the factorial is:', res)
