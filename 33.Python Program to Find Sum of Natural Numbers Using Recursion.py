def sum(n):
    if n==1:
        return n
    else :
        return n+sum(n-1)
n=int(input('enter a number : '))

if n<0:
    print('enter a positive value')
elif n==0:
    print('sum of 0 is 0')
else:
    print(sum(n))