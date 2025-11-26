num=int(input("enter the number : "))
if num==0 or num==1:
    print(f"{num} is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is prime")