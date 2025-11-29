# Python Program to Find HCF or GCD

num1=int(input('enter first number : '))
num2=int(input('enter second number : '))
arr1=list(filter(lambda a:num1%a==0,range(1,num1+1)))
arr2=list(filter(lambda a:num2%a==0,range(1,num2+1)))

arr1.sort(reverse=True)
arr2.sort(reverse=True)

hcf=None
for x in arr2:
    if x in arr1:
        hcf=x
        break

print(f"the hcf is : {hcf}")




# solution 2
num1=int(input('enter first number : '))
num2=int(input('enter second number : '))

if num1>num2:
    small=num2
else:
    small=num1

for i in range(1,small+1):
    if (num1%i==0)and (num2%i==0):
        hcf=i
print(f"the hcf is {hcf}")

    
        