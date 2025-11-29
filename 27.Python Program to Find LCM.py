from math import gcd
num1=int(input('enter first number : '))
num2=int(input('enter second number : '))

lcm=(num1*num2)/gcd(num1,num2)
print(int(lcm))