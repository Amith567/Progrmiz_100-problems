def factorial(num):
    if num<=1:
        return 1
    else:
        sum=1
        for fact in range(2,num+1):
            sum*=fact
        return sum

num=int(input("enter a number : "))
result=factorial(num)
print(f"factorial of {num} is {result}")