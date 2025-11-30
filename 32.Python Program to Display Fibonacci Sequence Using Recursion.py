def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
n=int(input('enter the number : '))
if n<0:
    print('no negative values')
else:
    for i in range(n):
        print(fib(i))