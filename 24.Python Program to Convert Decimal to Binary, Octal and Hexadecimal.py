run=True
while run:
    print("1.dec to bin")
    print('2.oct to hex')
    print('3.exit')
    choice=int(input('enter your choice : '))
    if choice==1:
        num=int(input('enter the value : '))
        print(f"decimal {num} is equivalent to {bin(num)} in binary")
    elif choice==2:
        num=int(input('enter the value : '))
        print(f"oct {oct(num)} is equivalent to {hex(num)} in hex")
    elif choice==3:
        exit()        
    else:
        print("invalid choice")
    next=(input("do you want to continue  (y/n) : "))
    run=(next=="y")