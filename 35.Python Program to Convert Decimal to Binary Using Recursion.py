def tobinary(n):
    if n>1:
        tobinary(n//2)
    print(n%2,end='')

n=int(input('enter a number : '))
print(f"there binary of {n} is",end=' ')
tobinary(n)
