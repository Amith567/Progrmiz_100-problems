num=input("enter the number : ")
sum=0
for digi in num:
    sum=sum+(int(digi))**3

print(f"{num} is armstrong" if sum==int(num) else f"{num} is not armstrong")