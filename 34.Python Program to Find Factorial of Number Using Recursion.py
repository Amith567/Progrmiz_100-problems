def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
    
n=int(input('enter a number : '))
print(f"the factorial of {n} terms is {factorial(n)}")