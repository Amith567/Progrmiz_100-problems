inp=input('enter a string : ')
if inp==inp[::-1]:
    print(f'{inp} is palindrome')
else:
    print(f'{inp} isn\'t palindrome')