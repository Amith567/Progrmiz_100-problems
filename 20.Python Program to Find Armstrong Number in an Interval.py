start=int(input("enter the starting number : "))
stop=int(input("enter the ending number : "))
armstrong=[]
for num in range(start,stop):
    sum=0
    for i in str(num):
        sum=sum+int(i)**3
    if sum==num:
        armstrong.append(sum)
if armstrong:
    print(*armstrong)
else:
    print(f"no armstrong number between {start} and {stop}")
