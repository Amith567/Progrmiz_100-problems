# Python Program to Find HCF or GCD

num=int(input("enter a number : "))
limit=int(num/2)+1
hcf=[]
for i in range (2,limit):
    if num%i==0:
        hcf.append(i)
print(f"the highest common factor of {num} is {max(hcf)}" if hcf else f"{num} has no factors")