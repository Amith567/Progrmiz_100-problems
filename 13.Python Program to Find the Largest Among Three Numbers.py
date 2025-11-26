print("enter the three numbers")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c :
    print(f"{a} is big")
elif b>c:
    print(f"{b} is big")
else:
    print(f"{c} is big")