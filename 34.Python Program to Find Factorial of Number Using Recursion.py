def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
n=int(input('enter a number : '))
if n<0:
    print('no negative values ')
elif n==0:
    print('factorial of 0 is 1')
else:
    print(f"the factorial of {n} terms is {factorial(n)}")