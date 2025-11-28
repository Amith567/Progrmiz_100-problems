num=int(input('enter a number : '))
limit=num//2+1
factors=[]
for item in range(1,limit):
    if num%item==0:
        factors.append(item)
print(f"factor of {num} is ",*factors if factors else f"no factors for {num}")
