# Python Program to Find the Factors of a Number
num=int(input('enter the number : '))
factors=list(filter((lambda x: num%x==0),range(1,num+1)))
print(*factors)